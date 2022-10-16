from django.db import models

# Create your models here.
# This is the family-data model

# This is the family-identification model
class CampModel(models.Model):
    camp_name = models.CharField(max_length=100)
    address = models.TextField()
class FamilyModel(models.Model):
    family_head_name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=14)
    camp = models.ForeignKey(CampModel, on_delete=models.CASCADE)
    def numbers_of_members(self):
        return len(self.family_set)
    
    def numbers_of_minors(self):
        return len(self.family_set.filter(age__lt=15))
    
    def numbers_of_women(self):
        return len(self.family_set.filter(gender="female", age__gt=35))
class OccupantModel(models.Model):
    name = models.CharField(max_length=14)
    age = models.IntegerField()
    GENDER_CHOICE = (('M', "male"), ("F", "female"))
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE)
    #CONDITION_CHOICE = (("pregnant", "pregnant"))
    #condition = models.CharField(choice=CONDITION_CHOICE)
    disabled = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=14)
    family = models.ForeignKey(FamilyModel, on_delete=models.CASCADE)
class private_request(models.Model):
    phone_no=models.CharField(max_length=14)
    first_name=models.CharField(max_length=14)
    requestt=models.CharField(max_length=200)
    def __str__(self):
        return self.requestt

