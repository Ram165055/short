from django.db import models
from phone_field import PhoneField

# Create your models here.
class Destination(models.Model):
    # id:int
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')
