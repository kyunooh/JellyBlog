from django.test import TestCase
from .models import Note

# Create your tests here.
class NoteViewTest(TestCase):

    def get_note(self):
        Note.create(content='note 1')
        
