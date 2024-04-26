from django.test import TestCase
from django.shortcuts import reverse
from .models import Note

class NotesListViewTest(TestCase):
    def setUp(self):
        self.note_obj = Note.objects.create(author='kia', text='Sample text.')

    def test_notes_list_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_notes_list_view_url_by_name(self):
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)

    def test_notes_list_page(self):
        response = self.client.get(reverse('notes_list'))
        self.assertContains(response, self.note_obj.text)
