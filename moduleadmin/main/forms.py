from django import forms
from .models import Role, Usuario

<<<<<<< HEAD

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
=======
class CreateNewUser(forms.ModelForm):
    class Meta:
         model = Usuario
         fields = ['name', 'last_name', 'role']

class UpdateUser(forms.ModelForm):
     class Meta:
         model = Usuario
         fields = ['name', 'last_name', 'role']
>>>>>>> 626311025f64afb4f177ebb1fc9a7df42744de22
