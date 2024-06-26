# Generated by Django 5.0.6 on 2024-06-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_api', '0002_alter_infoservice_finishdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoservice',
            name='finishDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoservice',
            name='startDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoservice',
            name='totalTime',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
