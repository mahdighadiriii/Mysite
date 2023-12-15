from django.shortcuts import render
from website.forms import ContactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for your message')
        else:
            messages.add_message(request, messages.ERROR, 'Form is not valid')
            
        
        
    form = ContactForm()
        
    context = {
    'form': form
    }

    return render(request, 'website/contact.html', context)


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')




def test_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you for your message')
        else:
            return HttpResponse('Form is not valid')

    form = ContactForm()
    context = {
        'form': form
    }

    return render(request, 'website/test.html', context)