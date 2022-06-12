from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Value as V
from django.core.paginator import Paginator
from django.db.models.functions import Concat
from django.contrib import messages
from .models import Contact


def home(request):
    contacts = Contact.objects.all().filter(
        to_show=True
    ).order_by('first_name')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agenda/pages/home.html', context={
        'contacts': page_obj
    })


def search(request):
    term = request.GET.get('term')

    if term is None or not term:
        messages.add_message(
            request,
            messages.ERROR,
            'Opss! campo de busca vazio.'
            )
        return redirect('agenda:home')

    field_search_contact = Concat('first_name', V(' '), 'last_name')
    contacts = Contact.objects.annotate(
        full_name=field_search_contact
    ).filter(
        Q(full_name__icontains=term) |
        Q(telephone__icontains=term),
        to_show=True
    )

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if len(contacts.values()) == 0:
        messages.add_message(
            request,
            messages.WARNING,
            '%i contato(s) encontrados' % (len(contacts.values()))
            )
    else:
        messages.add_message(
            request,
            messages.SUCCESS,
            '%i contato(s) encontrados' % (len(contacts.values()))
            )
    return render(request, 'agenda/pages/search_contact.html', context={
        'contacts': page_obj
    })


def contact(request, id_contact):
    contact = get_object_or_404(Contact, id=id_contact)
    return render(request, 'agenda/pages/contact.html', context={
        'contact': contact
    })
