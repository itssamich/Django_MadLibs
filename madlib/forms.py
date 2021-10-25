from django import forms
from .models import Madlib

class libForm(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['type1', 'type2', 'type3', 'type4', 'type5', 'type6', 'type7']