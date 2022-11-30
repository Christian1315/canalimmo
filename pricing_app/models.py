from django.db import models

# from agencies_app.models import Agency
# from agents_app.models import Agent

# Create your models here.

class Pricing(models.Model):
    price = models.IntegerField()
    type = models.CharField(max_length=100)

    #===== THE RELATIONSHIPS ======#
    # agent = models.ForeignKey(Agent,related_name='agent',on_delete=models.CASCADE)
    # agency = models.ForeignKey(Agency,related_name='agency',on_delete=models.CASCADE)


    def __str__(self):
        return self.price