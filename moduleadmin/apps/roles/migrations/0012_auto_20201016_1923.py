# Generated by Django 3.1 on 2020-10-17 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0011_auto_20201016_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='forma',
            new_name='formas',
        ),
    ]