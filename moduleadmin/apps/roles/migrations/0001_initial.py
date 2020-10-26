# Generated by Django 3.1 on 2020-10-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('insert', models.BooleanField()),
                ('update', models.BooleanField()),
                ('delete', models.BooleanField()),
                ('search', models.BooleanField()),
            ],
        ),
    ]
