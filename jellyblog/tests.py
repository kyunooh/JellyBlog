from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.test.testcases import LiveServerTestCase

from selenium import webdriver
from jellyblog.views import index, search_documents, init_category
from .models import Category, Note, Document


class NoteViewTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.note_content1 = "note test 111"
        self.note_content2 = "note test 222"
        Note.objects.create(content=self.note_content1)
        Note.objects.create(content=self.note_content2)

    def tearDown(self):
        self.browser.quit()

    def test_get_notes(self):
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url + reverse("blog_index"))
        elem = self.browser.find_element_by_xpath("//*")
        index_html = elem.get_attribute("outerHTML")

        self.assertIn(self.note_content1, index_html)
        self.assertIn(self.note_content2, index_html)


class DocumentViewTest(LiveServerTestCase):
    def setUp(self):
        init_category()
        category = Category.objects.get(name="Home")
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


class DocumentSearchTest(LiveServerTestCase):
    def setUp(self):
        init_category()
        category = Category.objects.get(name="Home")
        self.searchTestDoc1 = Document.objects.create(
            category=category,
            title="Document Search Test Document",
            content="Search Document Content1 It Would Be Found",
            meta_tag="searchsearchesarchesarchsearch",
            public_doc=True
        )

        self.notPublicDoc = Document.objects.create(
            category=category,
            title="It's not Public doc",
            content="It is not found cause, this is not public",
            meta_tag="metametametametametametamteamteatmeatm",
            public_doc=False
        )

        self.notFoundDoc1 = Document.objects.create(
            category=category,
            title="Not Found Document",
            content="This content is not found",
            meta_tag="searchsearchesarchesarchsearch",
            public_doc=False
        )

        self.notFoundDoc2 = Document.objects.create(
            category=category,
            title="Not found notnot found",
            content="This Content is not found",
            meta_tag="notnotnotnotnot foundounfdouynfdounfdounfd",
            public_doc=True
        )

    def test_search(self):
        request = HttpRequest()
        request.POST["search_query"] = "It Would Be Found"
        response = search_documents(request)

        self.assertIn(self.searchTestDoc1.title, response.content.decode())
        self.assertNotIn(self.notFoundDoc1.title, response.content.decode())
        self.assertNotIn(self.notFoundDoc2.title, response.content.decode())

    def test_not_fount_when_not_public_doc(self):
        request = HttpRequest()
        query = "It's not public doc"
        request.POST["search_query"] = query
        response = search_documents(request)

        self.assertNotIn(self.notPublicDoc.title, response.content.decode())
