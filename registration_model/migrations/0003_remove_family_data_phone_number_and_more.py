# Generated by Django 4.0.5 on 2022-10-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_model', '0002_family_data_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family_data',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='family_data',
            name='number_of_kids',
            field=models.IntegerField(default=None),
        ),
    ]
