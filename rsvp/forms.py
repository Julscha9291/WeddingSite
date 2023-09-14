
from django import forms
from .models import Guest

class RSVPForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'guests', 'attendance']
        
        