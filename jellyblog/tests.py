from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.test import TestCase
from django.test import override_settings
from django.test.testcases import LiveServerTestCase

from selenium import webdriver
from jellyblog.views import index
from .models import Category, Note, Document


class NoteViewTest(LiveServerTestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.note_content1 = "note test 111"
        self.note_content2 = "note test 222"
        Note.objects.create(content=self.note_content1)
        Note.objects.create(content=self.note_content2)

    def tearDown(self):
        self.browser.quit()

    def test_get_notes(self):
        self.browser.implicitly_wait(5)
        self.browser.get(self.live_server_url + reverse("blog_index"))
        elem = self.browser.find_element_by_xpath("//*")
        source_code = elem.get_attribute("outerHTML")

        self.assertIn(self.note_content1, source_code)
        self.assertIn(self.note_content2, source_code)


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


