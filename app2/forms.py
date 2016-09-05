from django import forms
from . import models

class AForm(forms.ModelForm):
    class Meta:
        model = models.A
        fields = '__all__'

class BForm(forms.ModelForm):
    class Meta:
        model = models.B
        fields = '__all__'

