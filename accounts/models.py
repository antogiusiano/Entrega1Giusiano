from django.db import models
from django.contrib.auth.models import User

class UserExtension(models.Model):
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    mas_descripcion = models.CharField(max_length=100)
