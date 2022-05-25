from pyexpat import model
from socket import fromshare
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = {'name', 'email', 'message'}
        labels = {'name': 'Name', 'email': 'Email', 'message': 'Message'}
