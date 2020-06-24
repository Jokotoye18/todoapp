from django.test import TestCase
from contact.models import Contact


class ContactModelTest(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            name = 'contact_name',
            email = 'contact@gmail.com',
            message = 'Checking on you dude'
        )

    def test_contact_text_representation(self):
        self.assertEqual(f'{self.contact}', 'contact@gmail.com')
        self.assertEqual(Contact.objects.count(), 1)

    def test_contact_content(self):
        contact = Contact.objects.get(pk=1)
        self.assertEqual(f'{contact.name}', 'contact_name')
        self.assertEqual(f'{contact.email}', 'contact@gmail.com')
        self.assertEqual(f'{contact.message}', 'Checking on you dude')



