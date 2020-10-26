from django.db import models

# Create your models here.

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    insert = models.BooleanField()
    edit = models.BooleanField()
    delete = models.BooleanField()
    search = models.BooleanField()
    formas = models.ManyToManyField("formas.FormsMenu", related_name="formas")

    def __str__(self):
        return self.name