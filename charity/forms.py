from django import forms
from django.forms import PasswordInput


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, required=False)
    password = forms.CharField(widget=PasswordInput(), required=True)


