from django.shortcuts import render
from django.views import View

from app2.models import Maqola


class AsosiyView(View):
    def get(self,request):
        m=Maqola.objects.all()
        return render(request,"asosiy.html",{"maqola":m})

class SarlavhaView(View):
    def get(self,request):
        s=Maqola.objects.get(id=pk)
        return render(request,"sarlavha.html",{"sarlavha":s})

