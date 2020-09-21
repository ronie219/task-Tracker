from django.urls import path

from .views import accountCreationAPI

urlpatterns = [
    path('create/',accountCreationAPI.as_view(),name ='create'),
]