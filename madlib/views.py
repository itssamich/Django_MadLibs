from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Madlib
from django import forms
from .forms import libForm

# Create your views here.
def index(request):
    libList = Madlib.objects.all()
    context = {
        'libList': libList,
    }
    return render(request, 'madlib/index.html', context)

def game(request, madlibId):
    lib = Madlib.objects.get(pk=madlibId)
    class libForm(forms.ModelForm):
        class Meta:
            model = Madlib
            fields = ['type1', 'type2', 'type3', 'type4', 'type5', 'type6', 'type7']
            labels = {
                'type1': lib.type1,
                'type2': lib.type2,
                'type3': lib.type3,
                'type4': lib.type4,
                'type5': lib.type5,
                'type6': lib.type6,
                'type7': lib.type7,
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
        return render(request, 'madlib/game' +str(madlibId)+'.html', {'arr':arr})

    return render(request, 'madlib/game.html', context)