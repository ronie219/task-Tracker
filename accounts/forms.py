from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import User


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        username = data.get('username')
        email = data.get('email')
        qs = User.objects.all()
        item = qs.filter(Q(username__icontains=username) | Q(email__iexact=email))
        if item.exists() == True:
            raise forms.ValidationError("User Alread Exixts")
        return super().clean(*args, **kwargs)
