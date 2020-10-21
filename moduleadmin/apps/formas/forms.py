from django import forms
from .models import FormsMenu


class CreateNewFormsMenu(forms.ModelForm):
    class Meta:
        model = FormsMenu
        fields = ['name', 'url', 'icon']
        error_messages = {
            'name': {
                'required': "Name es requerido",
            },
            'url': {
                'required': "Url es requerido",
            },
            'icon': {
                'required': "Icon es requerido",
            },
        }


class UpdateFormsMenu(forms.ModelForm):
    class Meta:
        model = FormsMenu
        fields = ['name', 'url', 'icon']
        error_messages = {
            'name': {
                'required': "Name es requerido",
            },
            'url': {
                'required': "Url es requerido",
            },
            'icon': {
                'required': "Icon es requerido",
            },
        }