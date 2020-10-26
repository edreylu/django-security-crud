# Generated by Django 3.1 on 2020-10-17 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formas', '0002_formsmenu_enabled'),
        ('roles', '0008_role_forma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='forma',
        ),
        migrations.AddField(
            model_name='role',
            name='forma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forma', to='formas.formsmenu'),
        ),
    ]
