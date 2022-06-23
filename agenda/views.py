from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Value as V
from django.core.paginator import Paginator
from django.db.models.functions import Concat
from django.contrib import messages
from .models import Contact
from .forms import NewContactForm


def home(request):
    contacts = Contact.objects.all().filter(
        to_show=True
    ).order_by('first_name')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = NewContactForm()

    return render(request, 'agenda/pages/home.html', context={
            'contacts': page_obj,
            'form': form
        }
    )


def add_contact(request):
    if request.method == 'POST':
        form = NewContactForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Contato %s %s adicionado com sucesso.' % (
                        first_name,
                        last_name
                    )
            )
            return redirect('agenda:home')


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
    form = NewContactForm(instance=contact)
    return render(request, 'agenda/pages/contact.html', context={
            'contact': contact,
            'form': form
        }
    )


def delete(request, id_contact_delete):
    contact_delete = get_object_or_404(Contact, id=id_contact_delete)
    contact_delete.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        'Contato %s %s apagado com sucesso.' % (
            contact_delete.first_name,
            contact_delete.last_name
        )
    )
    return redirect('agenda:home')


def update(request, id_contact_update):
    if request.method == 'POST':
        contact = get_object_or_404(Contact, id=id_contact_update)
        form = NewContactForm(
                request.POST,
                request.FILES or None,
                instance=contact
            )

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Contato atualizado com sucesso.'
            )
            return redirect('agenda:contact', contact.id)
