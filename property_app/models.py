from django.db import models


# Create your models here.

class PropertyQty(models.Model):
    type = models.CharField(max_length=100)
    room = models.IntegerField()
    garage = models.IntegerField()
    year = models.CharField(max_length=100)
    pipscine = models.BooleanField(default=False)
    area = models.IntegerField()

class PropertyFeature(models.Model):
    airCondition = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    terrace = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    bedding = models.BooleanField(default=False)
    microOnde = models.BooleanField(default=False)
    balCon = models.BooleanField(default=False)
    plage = models.BooleanField(default=False)
    chauffage = models.BooleanField(default=False)
    fumage = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)

class PropertyRating(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    title = models.CharField(max_length=100)
    email = models.EmailField()
    ratingAdded = models.IntegerField()

class PropertyContact(models.Model):
    email = models.EmailField()
    ratingAdded = models.IntegerField()
    phone = models.CharField(max_length=100)

class Property(models.Model):
    propImg = models.CharField(max_length=100)
    propTitle = models.CharField(max_length=300)
    gallery = models.CharField(max_length=600)
    adresse = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    propPrice = models.IntegerField()
    city = models.CharField(max_length=100)

    #===== THE RELATIONSHIPS ======#
    # publisher = models.ForeignKey(User,related_name='publisher' ,on_delete=models.CASCADE)
    # propQty = models.ForeignKey(PropertyQty,related_name='propQty' ,on_delete=models.CASCADE)
    # feature = models.ForeignKey(PropertyFeature,related_name='feature' ,on_delete=models.CASCADE)
    # rating = models.ForeignKey(PropertyRating,related_name='rating' ,on_delete=models.CASCADE)
    # contact = models.ForeignKey(PropertyContact,related_name='contact' ,on_delete=models.CASCADE)


    def __str__(self):
        return self.propTitle