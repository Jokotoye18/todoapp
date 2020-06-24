from django.test import TestCase
from todoapp.models import Todo
from django.contrib.auth import get_user_model

class TodoModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'user_test',
            email = 'user@gmail.com',
            password = '12345'
        )
        self.todo = Todo.objects.create(
            owner = self.user,
            title = 'Test title'
        )

    def  test_todo_model_text_representation(self):
        self.assertEqual(f'{self.todo}', 'Test title')
