from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin

from .models import User
from .forms import AccountCreationForm


class AccountCreationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = AccountCreationForm
    template_name = 'accounts/Registration.html'
    success_message = "Account created successfully"


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            send_mail('Success', 'The Password has been changed...', user.email, [user.email])
            return redirect('accounts:success')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form})


def success(request):
    return render(request, 'accounts/success.html')
