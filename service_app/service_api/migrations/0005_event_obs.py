# Generated by Django 5.0.6 on 2024-06-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_api', '0004_alter_vehicle_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='obs',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
