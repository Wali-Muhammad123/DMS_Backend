from rest_framework import serializers
from .models import Food,medicines,other_amenities
class Food_Serializer(serializers.Serializer):
    class Meta:
        model=Food
        fields=["food_id","food_name","food_type","food_quantity","food_price","food_description","food_image"]
class Medicines_Serializer(serializers.Serializer):
    class Meta:
        model=medicines
        fields=["medicine_id","medicine_name","medicine_type","medicine_quantity","medicine_price","medicine_description"]
class Other_amenities_Serializer(serializers.Serializer):
    class Meta:
        model=other_amenities
        fields=["amenity_id","amenity_name","amenity_type","amenity_quantity","amenity_price","amenity_description"]
