from django.forms import ModelForm
from django import forms
from ujumbe.models import Ujumbe

class FomuYaKutumaUjumbe(ModelForm):
    wapokeaji = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 3}))
    ujumbe = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    class Meta:
        model = Ujumbe
        fields = '__all__'
        exclude = ['user', 'kata']
    