
from django.test import TestCase
from .models import Todo
from django.utils import timezone
from django.core.urlresolvers import reverse

class TodoTest(TestCase):
    # models test
    def create_todo(self, title="To do title", text="To do title test"):
        return Todo.objects.create(title=title, text=text, created_at=timezone.now())

    def test_todo_creation(self):
        todo = self.create_todo()
        self.assertTrue(isinstance(todo, Todo))
        self.assertEqual(todo.__str__(), todo.title)

    # views test
    def test_todos_list_view(self):
        resp = self.client.get('/todos') 
        self.assertEqual(resp.status_code, 301)
    
    def test_admin_view(self):
        resp = self.client.get('/admin') 
        self.assertEqual(resp.status_code, 301)

    def test_add_view(self):
        resp = self.client.get('/todos/add') 
        self.assertEqual(resp.status_code, 200)

    def test_details_view(self):
        resp = self.client.get('/todos/details/2') 
        self.assertEqual(resp.status_code, 301) 
