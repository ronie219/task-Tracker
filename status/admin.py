from django.contrib import admin
from .models import Tasks
from .forms import StatusForm

class StatusadminForm(admin.ModelAdmin):
    # form = StatusForm
    # model = Tasks
    list_display = ['user','detail','percentange','created_at']

admin.site.register(Tasks,StatusadminForm)
