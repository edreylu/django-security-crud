# Generated by Django 3.1.1 on 2020-09-25 16:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20200925_1146'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Usuario',
        ),
    ]