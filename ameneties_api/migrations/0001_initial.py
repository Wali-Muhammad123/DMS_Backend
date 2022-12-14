# Generated by Django 4.0.5 on 2022-10-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=50)),
                ('food_type', models.CharField(max_length=50)),
                ('food_quantity', models.IntegerField()),
                ('food_price', models.IntegerField()),
                ('food_description', models.CharField(max_length=100)),
                ('food_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='medicines',
            fields=[
                ('medicine_id', models.AutoField(primary_key=True, serialize=False)),
                ('medicine_name', models.CharField(max_length=50)),
                ('medicine_type', models.CharField(max_length=50)),
                ('medicine_quantity', models.IntegerField()),
                ('medicine_price', models.IntegerField()),
                ('medicine_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='other_amenities',
            fields=[
                ('amenity_id', models.AutoField(primary_key=True, serialize=False)),
                ('amenity_name', models.CharField(max_length=50)),
                ('amenity_type', models.CharField(max_length=50)),
                ('amenity_quantity', models.IntegerField()),
                ('amenity_price', models.IntegerField()),
                ('amenity_description', models.CharField(max_length=100)),
            ],
        ),
    ]
