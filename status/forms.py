from django import forms
from django.contrib.auth import get_user_model

from .models import Tasks
User = get_user_model()

class StatusForm(forms.ModelForm):
    percentange = forms.IntegerField(required=True)
    starting_date = forms.DateField(required=True)
    class Meta:
        model = Tasks
        fields = [
            'detail',
            'starting_date',
            'percentange',
            'comment',
        ]
        widget = {
            'starting_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),         
        }
    def clean(self,*args, **kwargs):
        detail = self.cleaned_data['detail']
        percent = self.cleaned_data['percentange']
        if detail == '' or None:
            raise forms.ValidationError("Deatil Cannot be Blank")
        if int(percent) > 100:
            raise forms.ValidationError("Enter correct percent")
        return super().clean(*args, **kwargs)