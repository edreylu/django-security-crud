# Generated by Django 3.1 on 2020-10-11 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200929_1349'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FormsMenu',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='role',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
