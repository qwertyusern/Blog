from django.contrib.auth.models import User
from django.db import models

class Muallif(models.Model):
    ism=models.CharField(max_length=40)
    kasb=models.CharField(max_length=40)
    resm=models.FileField(upload_to="rasmlar")
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism