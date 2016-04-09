from django.http import HttpRequest
from django.test import TestCase

from jellyblog.views import index_with_page
from .models import Note


class NoteViewTest(TestCase):
    def setUp(self):
        self.note_content1 = "note test 111"
        self.note_content2 = "note test 222"
        Note.objects.create(content=self.note_content1)
        Note.objects.create(content=self.note_content2)

    def test_get_notes(self):
        request = HttpRequest()
        response = index_with_page(request)

        self.assertIn(self.note_content1, response.content.decode())
        self.assertIn(self.note_content2, response.content.decode())
