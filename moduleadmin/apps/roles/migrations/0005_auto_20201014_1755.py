# Generated by Django 3.1 on 2020-10-14 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formas', '0001_initial'),
        ('roles', '0004_auto_20201013_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolesforma',
            name='id_forma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idforma', to='formas.formsmenu'),
        ),
        migrations.AlterField(
            model_name='rolesforma',
            name='id_role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idrole', to='roles.role'),
        ),
    ]