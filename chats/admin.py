# chats/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Chat, Message, KnowledgeBase, AIMessage, AIChat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'display_participants',
                    'created_at', 'view_chat_link']
    search_fields = ['name']
    fieldsets = (
        (None, {
            'fields': ('name', 'participants')
        }),
    )

    def display_participants(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])
    display_participants.short_description = "Participants"

    def view_chat_link(self, obj):
        return format_html(f'<a href="/chat/chats/{obj.pk}">View Chat</a>')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(participants=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        return super().save_model(request, obj, form, change)

    # Permissions
    # def has_add_permission(self, request):
    #     if request.user.is_superuser:
    #         return super().has_add_permission(request)

    # def has_change_permission(self, request, obj=...):
    #     if request.user.is_superuser:
    #         return super().has_change_permission(request, obj)

    # def has_delete_permission(self, request, obj=...):
    #     if request.user.is_superuser:
    #         return super().has_delete_permission(request, obj)


@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ('topic', 'content')
    search_fields = ('topic', 'content')

    def has_view_permission(self, request, obj=...):
        if request.user.is_superuser:
            return super().has_view_permission(request, obj)

    # def has_add_permission(self, request):
    #     if request.user.is_superuser:
    #         return super().has_add_permission(request)

    # def has_change_permission(self, request, obj=...):
    #     if request.user.is_superuser:
    #         return super().has_change_permission(request, obj)

    # def has_delete_permission(self, request, obj=...):
    #     if request.user.is_superuser:
    #         return super().has_delete_permission(request, obj)


@admin.register(AIChat)
class AIChatAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at', 'view_chat_link']

    def view_chat_link(self, obj):
        return format_html(f'<a href="/chat/ai-chats/{obj.pk}">View AI Chat</a>')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        return super().save_model(request, obj, form, change)

    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
    )

    def has_delete_permission(self, request, obj=...):
        if request.user.is_superuser:
            return super().has_delete_permission(request, obj)
