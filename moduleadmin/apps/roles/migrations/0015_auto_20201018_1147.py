# Generated by Django 3.1 on 2020-10-18 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0014_auto_20201017_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='update',
            new_name='edit',
        ),
    ]
