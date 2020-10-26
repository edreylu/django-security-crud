from django import forms
from .models import Role


class CreateNewRole(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name','insert','edit','delete','search','formas']
        error_messages = {
            'name': {
                'required': "Name es requerido",
            },
            'formas': {
                'required': "Formas es requerido",
            },
        }


class UpdateRole(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name','insert','edit','delete','search','formas']
        error_messages = {
            'name': {
                'required': "Name es requerido",
            },
            'formas': {
                'required': "Formas es requerido",
            },
        }
