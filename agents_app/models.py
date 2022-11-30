from django.db import models

# import property_app.models as AProperty
# import pricing_app.models as APricing

# Create your models here.

class Agent(models.Model):
    imgProfile = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    propertyNum = models.IntegerField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    #===== THE RELATIONSHIPS ======#
    # pricing = models.ForeignKey(AProperty.Property,related_name='pricing',on_delete=models.CASCADE)
    # property = models.ForeignKey(APricing.Pricing,related_name='property',on_delete=models.CASCADE)

    def __str__(self):
        return self.name