from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Madlib
from django import forms

# Create your views here.
def index(request):
    libList = Madlib.objects.all()
    context = {
        'libList': libList,
    }
    return render(request, 'madlib/index.html', context)

def game(request, madlibId):
    lib = Madlib.objects.get(pk=madlibId)

    class libForm(forms.Form):
        lib = Madlib.objects.get(pk=madlibId)
        def __init__(self, *args, **kwargs):
            for i in range(1, lib.blankCount+1):
                field_name = eval('lib.type'+str(i))
                self.fields[field_name] = forms.CharField(required=True)

    
    form = libForm(request.POST or None)
    context = {
        'lib': lib,
        'form': form,
    }
    

    return render(request, 'madlib/game.html', context)