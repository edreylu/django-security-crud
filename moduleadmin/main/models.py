from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    insert = models.BooleanField()
    update = models.BooleanField()
    delete = models.BooleanField()
    search = models.BooleanField()

    def __str__(self):
        return self.name

class FormsMenu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    icon = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user", null=True, blank=False)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role", null=True, blank=False)

    def __str__(self):
        return self.name 