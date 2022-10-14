from django.db import models

# Create your models here.
# This is the family-data model
class Family_data(models.Model):
    family_id=models.AutoField(primary_key=True)
    family_head_name=models.CharField(max_length=50)
    number_of_members=models.IntegerField()
    number_of_minors=models.IntegerField()
    number_of_seniors=models.IntegerField()
    number_of_women=models.IntegerField()
    presence_of_pregnant=models.IntegerField(choices=((0,'No'),(1,'Yes')))
    presence_of_disabled=models.IntegerField(choices=((0,'No'),(1,'Yes')))
    class Meta:
        abstract=True
# This is the family-identification model
