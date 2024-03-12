from django.contrib import admin
from chat.models import Message, Chat


class MessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Message model.
    This class specifies the fields to display in the admin interface,
    the list display fields, and the search fields for filtering messages.
    """
    fields = ("chat", "text", "created_at", "author", "receiver")
    list_display = ("created_at", "author", "text", "receiver")
    search_fields = ("text",)


# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
