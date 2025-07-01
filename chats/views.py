# chats/views.py
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Chat, Message, KnowledgeBase, AIChat, AIMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from asgiref.sync import sync_to_async
from django.http import JsonResponse, HttpResponse
import asyncio
from django.contrib.auth.decorators import login_required
from django.db.models import Max
import requests
from django.contrib.auth import get_user_model
import os


User = get_user_model()


# AI VIEW
API_KEY = os.environ.get('AI_API_KEY')


def call_openrouter_ai(user_message):

    knowledge_entries = KnowledgeBase.objects.all()

    knowledge_text = "\n\n".join(
        [f"Topic: {entry.topic}\nContent: {entry.content}" for entry in knowledge_entries]
    )

    system_prompt = f"""
    You are a helpful AI assistant for our company's ERP HR agency system.
    Your primary goal is to assist employees by providing accurate information based ONLY on the knowledge I provide you.
    If a user's question cannot be answered from the provided knowledge, politely say that you don't have information on that topic. Do not make things up.
    Answers must be as human as possible.

    --- KNOWLEDGE BASE ---
    {knowledge_text}
    --- END KNOWLEDGE BASE ---
    """

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
    }

    response = requests.post(url, json=data, headers=headers)
    reply_json = response.json()

    if 'choices' in reply_json:
        return reply_json['choices'][0]['message']['content']
    else:
        error_message = reply_json.get(
            'error', {}).get('message', 'Unknown error')
        raise ValueError(error_message)
        # return f"AI service error: {error_message}"

###


class AIChatDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        ai_chat = get_object_or_404(AIChat, pk=pk)
        ai_messages = ai_chat.ai_messages.order_by('timestamp')
        return render(request, 'chats/chat_detail.html', {'chat': ai_chat, 'messages': ai_messages, 'chat_type': 'ai'})

    def post(self, request, pk):
        ai_chat = get_object_or_404(AIChat, pk=pk)
        text = request.POST.get('text')
        if text:
            AIMessage.objects.create(
                chat=ai_chat, user=request.user, text=text)

            ai_reply = call_openrouter_ai(text)

            try:
                bot_user = User.objects.get(username='ChatBot')
            except User.DoesNotExist:
                bot_user = User.objects.create_user(
                    username='ChatBot')
                bot_user.set_unusable_password()
                bot_user.save()

            AIMessage.objects.create(
                chat=ai_chat, user=bot_user, text=ai_reply)

            return HttpResponse(status=204)
        return HttpResponse(status=400)


class ChatDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        chat = get_object_or_404(Chat, pk=pk)
        messages = chat.messages.order_by('timestamp')
        return render(request, 'chats/chat_detail.html', {'chat': chat, 'messages': messages, 'chat_type': 'regular'})

    def post(self, request, pk):
        chat = get_object_or_404(Chat, pk=pk)
        text = request.POST.get('text')
        if text:
            Message.objects.create(chat=chat, user=request.user, text=text)
            return HttpResponse(status=204)
        return HttpResponse(status=400)


@login_required
async def stream_chat_messages(request, pk):
    chat = await sync_to_async(get_object_or_404)(Chat, pk=pk)
    last_message_id_from_client = int(request.GET.get('last_id', 0))
    timeout_seconds = 20

    start_time = asyncio.get_event_loop().time()

    while True:
        new_messages_query = Message.objects.filter(
            chat=chat, id__gt=last_message_id_from_client
        ).select_related('user').order_by('timestamp')

        new_messages = await sync_to_async(list)(new_messages_query)

        if new_messages:
            messages_data = []
            for message in new_messages:
                messages_data.append({
                    'id': message.id,
                    'author': message.user.username,
                    'content': message.text,
                    'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                })
            return JsonResponse({'messages': messages_data})

        if asyncio.get_event_loop().time() - start_time > timeout_seconds:
            return JsonResponse({'messages': []})

        await asyncio.sleep(0.5)


# AI Stream
@login_required
async def stream_ai_chat_messages(request, pk):
    ai_chat = await sync_to_async(get_object_or_404)(AIChat, pk=pk)
    last_message_id_from_client = int(request.GET.get('last_id', 0))
    timeout_seconds = 20

    start_time = asyncio.get_event_loop().time()

    while True:
        new_messages_query = AIMessage.objects.filter(
            chat=ai_chat, id__gt=last_message_id_from_client
        ).select_related('user').order_by('timestamp')

        new_messages = await sync_to_async(list)(new_messages_query)

        if new_messages:
            messages_data = []
            for message in new_messages:
                messages_data.append({
                    'id': message.id,
                    'author': message.user.username,
                    'content': message.text,
                    'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                })
            return JsonResponse({'messages': messages_data})

        if asyncio.get_event_loop().time() - start_time > timeout_seconds:
            return JsonResponse({'messages': []})

        await asyncio.sleep(0.5)
