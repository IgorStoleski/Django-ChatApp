from django.test import TestCase
from django.contrib.auth import get_user_model
from chat.models import Chat, Message
from datetime import date

User = get_user_model()

class ChatMessageModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Erstellen von Benutzerinstanzen für Autor und Empfänger
        cls.author = User.objects.create_user(username='author', password='testpass123')
        cls.receiver = User.objects.create_user(username='receiver', password='testpass123')

        # Erstellen einer Chat-Instanz
        cls.chat = Chat.objects.create()

        # Erstellen einer Nachrichteninstanz
        cls.message = Message.objects.create(
            text="Hello, World!",
            chat=cls.chat,
            author=cls.author,
            receiver=cls.receiver
        )

    def test_chat_creation_date(self):
        """Testet, ob das Erstellungsdatum des Chats korrekt ist."""
        self.assertEqual(self.chat.created_at, date.today())

    def test_message_content(self):
        """Testet, ob der Inhalt der Nachricht korrekt gespeichert wird."""
        self.assertEqual(self.message.text, "Hello, World!")

    def test_message_chat_relation(self):
        """Testet die Beziehung zwischen Nachricht und Chat."""
        self.assertEqual(self.message.chat, self.chat)

    def test_message_author_and_receiver(self):
        """Testet, ob Autor und Empfänger der Nachricht korrekt zugeordnet werden."""
        self.assertEqual(self.message.author, self.author)
        self.assertEqual(self.message.receiver, self.receiver)

    def test_message_creation_date(self):
        """Testet, ob das Erstellungsdatum der Nachricht korrekt ist."""
        self.assertEqual(self.message.created_at, date.today())