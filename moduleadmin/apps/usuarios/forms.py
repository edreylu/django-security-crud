from django import forms
from .models import Usuario


class CreateNewUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'last_name', 'role', 'user']
        error_messages = {
            'name': {
                'required': "Name es requerido",
            },
            'last_name': {
                'required': "Last name es requerido",
            },
            'role': {
                'required': "Role es requerido",
            },
            'user': {
                'required': "User es requerido",
            },
        }


class UpdateUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'last_name', 'role', 'user']
        error_messages = {
            'name': {
                'required': "Name es requerido",
            },
            'last_name': {
                'required': "Last name es requerido",
            },
            'role': {
                'required': "Role es requerido",
            },
            'user': {
                'required': "User es requerido",
            },
        }
