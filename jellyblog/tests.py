from django.http import HttpRequest
from django.test import TestCase

from jellyblog.views import index
from .models import Category, Note, Document


class NoteViewTest(TestCase):
    def setUp(self):
        self.note_content1 = "note test 111"
        self.note_content2 = "note test 222"
        Note.objects.create(content=self.note_content1)
        Note.objects.create(content=self.note_content2)

    def test_get_notes(self):
        request = HttpRequest()
        response = index(request)

        self.assertIn(self.note_content1, response.content.decode())
        self.assertIn(self.note_content2, response.content.decode())


class DocumentViewTest(TestCase):
    def setUp(self):
        Category.init_category()
        category = Category.objects.get(pk=1)
        self.test_doc1 = Document.objects.create(
            category=category,
            title="Document Test",
            content="Content content content ",
            meta_tag="metametametametametameta",
            public_doc=True
        )

    def test_get_document(self):
        request = HttpRequest()
        response = index(request)

        self.assertIn(self.test_doc1.title, response.content.decode())


