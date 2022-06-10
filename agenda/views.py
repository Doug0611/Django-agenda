from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contact


def home(request):
    contacts = Contact.objects.all().order_by('first_name')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agenda/pages/home.html', context={
        'contacts': page_obj
    })


def contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)
    return render(request, 'agenda/pages/contact.html', context={
        'contact': contact
    })
