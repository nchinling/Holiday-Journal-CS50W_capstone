# Generated by Django 4.1.5 on 2023-07-20 10:58

import countries.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=countries.models.upload_to_photo),
        ),
    ]
