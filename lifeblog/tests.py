from django.test import LiveServerTestCase
from .models import Document


class DocumentTest(LiveServerTestCase):
    def setUp(self):
        test_public_doc = Document.objects.create(
            title="DocumentTest Title",
            content="DocumentTest Content content",
            meta_tag="metametametametametametametameta",
            public_doc=True)
        
        test_private_doc = Document.objects.create(
            title="DocumentTest private",
            content="DocumentTest Content content",
            meta_tag="metametametametametametametameta",
            public_doc=False)

    def test_public_doc(self):
        pass
