from django import forms
from .models import Publicar

class PubForm(forms.ModelForm):

    class Meta:
        model = Publicar
        fields = ('titulo', 'texto',)
