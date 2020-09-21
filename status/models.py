from django.db import models
from django.utils.timezone import now
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    starting_date = models.DateField(blank=True,default=now)
    percentange = models.IntegerField(default=0)
    detail = models.CharField(max_length=250)
    comment = models.CharField(max_length = 250,blank=True, default= ' ')

    def __str__(self):
        return self.detail
    
    def get_absolute_url(self):
        return reverse('status:detail', kwargs= {"pk":self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'percentange', 'updated_at']

    