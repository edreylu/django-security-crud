# Generated by Django 3.1 on 2020-10-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formas', '0002_formsmenu_enabled'),
        ('roles', '0012_auto_20201016_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='formas',
        ),
        migrations.RemoveField(
            model_name='rolesforma',
            name='id_forma',
        ),
        migrations.AddField(
            model_name='rolesforma',
            name='id_forma',
            field=models.ManyToManyField(related_name='formas', to='formas.FormsMenu'),
        ),
    ]
