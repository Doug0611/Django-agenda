from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Value as V
from django.core.paginator import Paginator
from django.db.models.functions import Concat
from .models import Contact


def home(request):
    contacts = Contact.objects.all().order_by('first_name')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agenda/pages/home.html', context={
        'contacts': page_obj
    })


def search(request):
    term = request.GET.get('term')

    if term is None:
        raise Http404()

    field_search_contact = Concat('first_name', V(' '), 'last_name')
    contacts = Contact.objects.annotate(
        full_name=field_search_contact
    ).filter(
        Q(full_name__icontains=term) |
        Q(telephone__icontains=term)
    )

    return render(request, 'agenda/pages/search_contact.html', context={
        'contacts': contacts
    })


def contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)
    return render(request, 'agenda/pages/contact.html', context={
        'contact': contact
    })
