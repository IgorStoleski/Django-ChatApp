from django.apps import AppConfig


class ChatConfig(AppConfig):
    """
    Configuration class for the 'chat' Django app.
    This class specifies the default auto field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
