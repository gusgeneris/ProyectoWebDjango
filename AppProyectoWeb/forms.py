
from django import forms

class ContactoForm (forms.Form):
    asunto= forms.CharField(max_length=50)
    email= forms.EmailField()
    mensaje= forms.CharField()
    