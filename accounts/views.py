from django.shortcuts import render, redirect
from accounts.forms import AccountForm
# from django.contrib import messages


def login(request):
    return render(request, 'accounts/pages/login.html')


def dashboard(request):
    return render(request, 'accounts/pages/dashboard.html')


def logout(request):
    return render(request, 'accounts/pages/logout.html')


def create_account(request):
    if request.method == 'POST':
        account = AccountForm(request.POST)

        if account.is_valid():
            return redirect('accounts:login')

    else:
        account = AccountForm()

    return render(request, 'accounts/pages/create_account.html', context={
        'form': account
        }
    )
