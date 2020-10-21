# Generated by Django 3.1 on 2020-10-12 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formas', '0001_initial'),
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolesForma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_status', models.BigIntegerField()),
                ('id_forma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_forma', to='formas.formsmenu')),
                ('id_role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_role', to='roles.role')),
            ],
        ),
    ]