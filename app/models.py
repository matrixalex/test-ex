from django.contrib.auth import admin
from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

"""
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_authentificated = models.BooleanField(default=False)
    class Meta:
        ordering = ["-username"]

    def __str__(self):
        return self.username
"""

class Admin(models.Model):
    #id = models.IntegerField(auto_created=True)
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username + ' is admin'

    class Meta:
        ordering = ["-username"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])


