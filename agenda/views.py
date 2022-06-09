from django.shortcuts import render, get_object_or_404
from .models import Contact


def home(request):
    contacts = Contact.objects.all()
    return render(request, 'agenda/pages/home.html', context={
        'contacts': contacts
    })


def contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)
    return render(request, 'agenda/pages/contact.html', context={
        'contact': contact
    })
