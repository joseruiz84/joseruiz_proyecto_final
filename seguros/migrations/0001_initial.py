# Generated by Django 4.1.7 on 2023-03-21 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Suma_asegurada', models.CharField(max_length=30)),
                ('Suma_description', models.CharField(max_length=80)),
                ('heading', models.CharField(max_length=15)),
            ],
        ),
    ]
