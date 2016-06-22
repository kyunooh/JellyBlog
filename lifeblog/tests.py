from django.test import LiveServerTestCase, Client
from .models import Document


class DocumentTest(LiveServerTestCase):
    def setUp(self):
        self.test_public_doc = Document.objects.create(
            title="DocumentTest Title",
            content="DocumentTest Content content",
            meta_tag="metametametametametametametameta",
            public_doc=True)
        
        self.test_private_doc = Document.objects.create(
            title="DocumentTest private",
            content="DocumentTest Content content",
            meta_tag="metametametametametametametameta",
            public_doc=False)

    def test_public_doc(self):
        c = Client()
        response = c.get("/lifeblog/")
        self.assertIn(self.test_public_doc.title, response.content.decode())
        self.assertNotIn(
            self.test_private_doc.title, response.content.decode())

    def test_document_detail(self):
        c = Client()
        response = c.get("/lifeblog/" + self.test_public_doc.pk)
        self.assertEquals(200, response.status_code)
        self.assertIn(self.test_public_doc.title, response.content.decode())
