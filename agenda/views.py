from django.shortcuts import render


def home(request):
    return render(request, 'agenda/pages/home.html')


def contact(request, id):
    return render(request, 'agenda/pages/contact.html')
