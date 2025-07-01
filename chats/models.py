from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Chat(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='created_chats')
    participants = models.ManyToManyField(
        CustomUser, related_name='participated_chats', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField(null=False, blank=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='messages')
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name='messages')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} in {self.chat}: {self.text[:20]}"


# ChatBot

class AIChat(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='created_ai_chats')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AIMessage(models.Model):
    text = models.TextField(null=False, blank=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='ai_messages')
    chat = models.ForeignKey(
        AIChat, on_delete=models.CASCADE, related_name='ai_messages')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} in {self.chat}: {self.text[:20]}"


class KnowledgeBase(models.Model):
    topic = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name = "Knowledge Base"
        verbose_name_plural = "Knowledge Base"

    def __str__(self):
        return self.topic
