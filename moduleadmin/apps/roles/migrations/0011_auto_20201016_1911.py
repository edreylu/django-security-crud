# Generated by Django 3.1 on 2020-10-17 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formas', '0002_formsmenu_enabled'),
        ('roles', '0010_auto_20201016_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='forma',
            field=models.ManyToManyField(related_name='formas', to='formas.FormsMenu'),
        ),
    ]
