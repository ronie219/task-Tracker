from django.shortcuts import render
from datetime import date
from django.contrib.auth import get_user_model
from status.models import Tasks

User  = get_user_model()

def Home(request):
    qs = Tasks.objects.filter(created_at=date.today())
    return render(request, 'home.html',{"today_detail":qs})


def test(request):
    return render(request, 'test.html',)


def thanks(request):
    return render(request, 'thanks.html',)