from django.shortcuts import render, redirect
from accounts.forms import UserAccountForm
from django.contrib.auth.models import User
# from django.contrib import messages


def login(request):
    return render(request, 'accounts/pages/login.html')


def dashboard(request):
    return render(request, 'accounts/pages/dashboard.html')


def logout(request):
    return render(request, 'accounts/pages/logout.html')


def create_account(request):
    if request.method == 'POST':
        account = UserAccountForm(request.POST)

        if account.is_valid():
            first_name = account.cleaned_data['first_name']
            last_name = account.cleaned_data['last_name']
            username = account.cleaned_data['username']
            email = account.cleaned_data['email']
            password = account.cleaned_data['password']

            User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )

            return redirect('accounts:login')
    else:
        account = UserAccountForm()

    return render(request, 'accounts/pages/create_account.html', context={
        'form': account
        }
    )
