from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class Table(models.Model):
  name = models.CharField(max_length=150, unique=True)
  link = models.URLField(max_length=200, unique=True)

  def __str__(self):
    return self.name

class CustomUser(models.Model):
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  photo = models.ImageField(upload_to='avatars/', null=True, blank=True)

  def __str__(self):
    return str(self.username)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)