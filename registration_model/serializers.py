
from rest_framework import serializers
from .models import OccupantModel,FamilyModel,CampModel,private_request
class OccupantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=OccupantModel
        fields=['name','age','gender','disabled','phone_no','family']
class FamilyModelSerializer(serializers.Serializer):
    class Meta:
        model=FamilyModel
        fields=['family_head_name','phone_no','camp','number_of_members','number_of_minors','number_of_women']
class CampModelSerializer(serializers.Serializer):
    class Meta:
        model=CampModel
        fields=['camp_name','address']
class private_requestSerializer(serializers.Serializer):
    class Meta:
        model=private_request
        fields=['phone_no','first_name','requestt']