# Generated by Django 3.1 on 2020-09-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200929_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]