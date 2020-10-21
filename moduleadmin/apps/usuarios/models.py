from django.db import models
from apps.roles.models import Role
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True, blank=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role", null=True, blank=False)

    def __str__(self):
        return self.name 