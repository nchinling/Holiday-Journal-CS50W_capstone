# Generated by Django 4.1.5 on 2023-07-23 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_destination_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_data', models.TextField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_image', to='countries.destination')),
            ],
        ),
    ]
