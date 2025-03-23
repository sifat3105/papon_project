from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    description = models.CharField(max_length=1, choices=[('a', 'Record Label'), ('b', 'Artist'), ('c', 'Distributor')])
    country = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username