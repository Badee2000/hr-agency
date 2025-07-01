# chats/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chats/<int:pk>/', views.ChatDetailView.as_view(), name='chat_detail'),
    path('ai-chats/<int:pk>/', views.AIChatDetailView.as_view(),
         name='ai_chat_detail'),
    # To be edited when I use WebSockets
    path('chats/<int:pk>/stream/', views.stream_chat_messages,
         name='stream_chat_messages'),
    path('ai-chats/<int:pk>/stream/',
         views.stream_ai_chat_messages, name='stream_ai_chat_messages')
]
 