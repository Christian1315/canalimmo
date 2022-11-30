from django.db import models
# from property_app.models import Property
# from agents_app.models import Agent
# from pricing_app.models import Pricing

# import property_app.models as AProperty 
# import agents_app.models as Aagent
# import pricing_app.models as APricing


# Create your models here.

class Agency(models.Model):
    imgProfile = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    agencyNum = models.IntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    description = models.TextField()

    #===== THE RELATIONSHIPS ======#

    # property = models.ForeignKey(Property, related_name='property', on_delete=models.CASCADE)
    # agent = models.ForeignKey(Agent, related_name='agent', on_delete=models.CASCADE)
    # pricing = models.ForeignKey(Pricing, related_name='pricing', on_delete=models.CASCADE)


    def __str__(self):
        return self.name