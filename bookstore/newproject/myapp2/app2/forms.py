from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import book,contact


class booksregistration(forms.ModelForm):
    class Meta:
        model = book
        fields = "__all__"

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields="__all__"