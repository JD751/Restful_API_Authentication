from django.db import models

# Create your models here.
class Holidays (models.Model):
    destination= models.CharField(max_length= 50, primary_key=True)
    number_of_days= models.IntegerField()
    Price_USD = models.IntegerField()
    holiday_type= models.CharField(max_length=20)