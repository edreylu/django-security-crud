# Generated by Django 3.1 on 2020-09-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200925_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='name',
            field=models.CharField(error_messages={'required': 'Please enter your name'}, max_length=200),
        ),
    ]
