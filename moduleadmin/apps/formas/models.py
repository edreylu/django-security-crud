from django.db import models

# Create your models here.

class FormsMenu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    icon = models.CharField(max_length=300)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name