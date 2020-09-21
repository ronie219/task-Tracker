from django.urls import path
from django.contrib.auth.views import (LoginView ,
                                        LogoutView,
                                        LogoutView)
# from django.contrib.auth.views import 

from .views import AccountCreationView,change_password,success

app_name = 'accounts'


urlpatterns = [
    path('create/',AccountCreationView.as_view(),name ='create'),
    path('login/', LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
    path('change_password/',change_password,name = 'change_password'),
    path('success/',success,name="success"),
]
