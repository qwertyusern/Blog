from django.db import models

from app1.models import Muallif


class Maqola(models.Model):
    sarlavha=models.CharField(max_length=120)
    sana=models.DateField(auto_now_add=True)
    matn=models.TextField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha

class Comment(models.Model):
    matn=models.CharField(max_length=200)
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE)
    sana=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.muallif