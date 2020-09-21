from django.contrib import admin
from .models import User
from django.contrib.auth.models import User as u

admin.site.register(User)
# admin.site.unregister(u)
