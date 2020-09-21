from django.db import models
from django.urls import reverse
from django.contrib.auth import models as u
from django.utils.timezone import timezone
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models.signals import post_save


class User(u.User):
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("accounts:login")

    # def save(self):
    #     send_mail('Thanks For Registering',
    #             'You successfully register and you username is  {}'.format(self.username),
    #             self.email,
    #             [self.email])
    #     return super().save()


def confirmationMail(sender, **kwargs):
    if kwargs['created']:
        send_mail('Thanks For Registering',
                  'You successfully register and you username is  {}'.format(kwargs['instance'].username),
                  kwargs['instance'].email,
                  [kwargs['instance'].email])


post_save.connect(confirmationMail, sender=User)
