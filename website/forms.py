from website.models import Contact
from django.forms import ModelForm
from django import forms

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
