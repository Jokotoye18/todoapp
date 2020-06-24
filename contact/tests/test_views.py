from django.test import TestCase
from django.urls import reverse
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


    def test_contact_view_status_code(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)

    def test_contact_view_by_view_name(self):
        resp = self.client.get(reverse('contact:contact'))
        self.assertEqual(resp.status_code, 200)

    def test_contact_view_template_used(self):
        resp = self.client.get(reverse('contact:contact'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact.html')

    def test_contact_view_post(self):
        self.client.post(reverse('contact:contact'), {
            'name': 'Contact test',
            'email': 'contact@gmail.com',
            'message': 'Testing'
        })
        self.assertEqual(Contact.objects.last().email, 'contact@gmail.com')

    
        
    
         

