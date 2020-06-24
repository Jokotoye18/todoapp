from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib import messages
from .models import Contact
from django.template.loader import get_template
from .forms import ContactForm
from django.views.generic import View


class ContactView(View):
    login_url = 'account_login'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {"form":form}
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            subject = 'Contact Form Received'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.DEFAULT_FROM_EMAIL]

            context = {
                'user': name,
                'email': email,
                'message': message
            }

            contact_message = get_template('contact_message.txt').render(context)

            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            form.save()
            messages.info(request, 'Your message has been received.')
        return redirect("todoapp:home")


