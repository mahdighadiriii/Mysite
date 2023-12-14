from website.models import Contact, Newsletter
from django.forms import ModelForm
from django import forms

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'