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
    @classmethod
    def setUpClass(cls):
        super(DocumentViewTest, cls).setUpClass()
        Category.init_category()

    def setUp(self):
        category = Category.objects.get(pk=1)
        self.test_doc1 = Document.objects.create(
            category=category,
            title="Document Test1",
            content="Content content content",
            meta_tag="metametametametametameta",
            public_doc=True
        )

        self.test_doc2 = Document.objects.create(
            category=category,
            title="Document Test2",
            content="Content2 content2 content2",
            meta_tag="metametametametametameta",
            public_doc=False
        )

    def test_get_document(self):
        request = HttpRequest()
        response = index(request)

        self.assertIn(self.test_doc1.title, response.content.decode())
        self.assertIn(self.test_doc1.content, response.content.decode())

    def test_about_private_doc(self):
        request = HttpRequest()
        response = index(request)
        self.assertNotIn(self.test_doc2.title, response.content.decode())
        self.assertNotIn(self.test_doc2.content, response.content.decode())


