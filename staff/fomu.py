from django.forms import ModelForm
from django import forms
from staff.models import UjumbeWaTangazo

class FomuYaKutumaTangazo(ModelForm):
    wapokeaji = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 3}))
    
    class Meta:
        model = UjumbeWaTangazo
        fields = '__all__'
        exclude = ['user',]