from django.shortcuts import render
from website.forms import ContactForm
from django.http import HttpResponse
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
            
        
        
    form = ContactForm()
        
    context = {
    'form': form
    }

    return render(request, 'website/contact.html', context)


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