from datetime import date
from django.conf import settings
from django.db import models

# Create your models here.

class Chat(models.Model):
    """
    This model represents a chatroom.
    It has a creation date.
    """
    created_at = models.DateField(default=date.today)


class Message(models.Model):
    """
    This model represents a message sent in a chatroom.
    It contains the text of the message, the creation date, 
    and references to the chat it belongs to, the author of the message,
    and the receiver of the message.
    """
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
