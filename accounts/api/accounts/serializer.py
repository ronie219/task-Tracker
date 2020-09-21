from rest_framework import serializers
from django.contrib.auth import get_user_model

usr = get_user_model()

from accounts.models import User
from accounts.forms import AccountCreationForm

class accountCreation(serializers.ModelSerializer):
    class Meta:
        model = User
        form =  AccountCreationForm
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
    
    def validate_username(self,value):
        qs = usr.objects.filter(username__iexact=value)
        if qs.exists:
            raise serializers.ValidationError("Username is already in DB")
        return value