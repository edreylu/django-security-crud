from django import forms
from .models import Role, Usuario

class CreateNewUser(forms.ModelForm):
    class Meta:
         model = Usuario
         fields = ['name', 'last_name', 'role']

class UpdateUser(forms.ModelForm):
     class Meta:
         model = Usuario
         fields = ['name', 'last_name', 'role']