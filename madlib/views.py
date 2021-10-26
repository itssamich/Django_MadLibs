from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Madlib
from django import forms
from .forms import libForm
import random

# Create your views here.
def index(request):
    libList = Madlib.objects.all()
    randomVal = random.randint(1, libList.count())
    print(randomVal)
    context = {
        'libList': libList,
        'randomVal': randomVal,
    }
    return render(request, 'madlib/index.html', context)

def game(request, madlibId):
    lib = Madlib.objects.get(pk=madlibId)
    class libForm(forms.ModelForm):
        class Meta:
            model = Madlib
            fields = ['type1', 'type2', 'type3', 'type4', 'type5', 'type6', 'type7', 'type8', 'type9', 'type10']
            labels = {
                'type1': lib.type1,
                'type2': lib.type2,
                'type3': lib.type3,
                'type4': lib.type4,
                'type5': lib.type5,
                'type6': lib.type6,
                'type7': lib.type7,
                'type8': lib.type8,
                'type9': lib.type9,
                'type10': lib.type10,
            }

    form = libForm(request.POST or None)


    context = {
        'lib': lib,
        'form': form,
    }
    
    if(form.is_valid()):
        arr = []
        for i in range(1, lib.blankCount+1):
            arr.append(form.cleaned_data.get('type' + str(i)))
        return render(request, 'madlib/stories/story'+ str(madlibId) + '.html', {'arr':arr, 'lib':lib})

    return render(request, 'madlib/game.html', context)