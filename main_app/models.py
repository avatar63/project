from django.db import models

# Create your models here.


class users(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    email =models.EmailField(max_length=200)
    is_ops=models.BooleanField(default=False)

class documents(models.Model):
    name =models.CharField(max_length=150)
    file = models.FileField(upload_to='files', blank=True, null=True)