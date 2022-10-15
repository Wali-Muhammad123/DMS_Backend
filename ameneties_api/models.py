from django.db import models

# Create your models here.
class Food(models.Model):
    food_id=models.AutoField(primary_key=True)
    food_name=models.CharField(max_length=50)
    food_type=models.CharField(max_length=50)
    food_quantity=models.IntegerField()
    food_price=models.IntegerField()
    food_description=models.CharField(max_length=100)
    food_image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.food_name
class medicines(models.Model):
    medicine_id=models.AutoField(primary_key=True)
    medicine_name=models.CharField(max_length=50)
    medicine_type=models.CharField(max_length=50)
    medicine_quantity=models.IntegerField()
    medicine_price=models.IntegerField()
    medicine_description=models.CharField(max_length=100)
    def __str__(self):
        return self.medicine_name
class other_amenities(models.Model):
    amenity_id=models.AutoField(primary_key=True)
    amenity_name=models.CharField(max_length=50)
    amenity_type=models.CharField(max_length=50)
    amenity_quantity=models.IntegerField()
    amenity_price=models.IntegerField()
    amenity_description=models.CharField(max_length=100)
    def __str__(self):
        return self.amenity_name