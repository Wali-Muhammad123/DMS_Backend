# Generated by Django 4.0.5 on 2022-10-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_model', '0005_occupantmodel_delete_family_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='private_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=14)),
                ('first_name', models.CharField(max_length=14)),
                ('requestt', models.CharField(max_length=200)),
            ],
        ),
    ]
