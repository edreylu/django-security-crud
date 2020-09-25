from django import forms
from .models import Role

class CreateNewUser(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    last_name = forms.CharField(label="LastName",max_length=200)
    role = forms.models.ModelChoiceField(label="Role",queryset=Role.objects)

class UpdateNewUser(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    last_name = forms.CharField(label="LastName",max_length=200)
    role = forms.models.ModelChoiceField(label="Role",queryset=Role.objects)