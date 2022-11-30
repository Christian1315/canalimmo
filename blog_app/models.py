from django.db import models

# Create your models here.
class BlogComments(models.Model):
    name = models.CharField(max_length=100)
    commentedDate = models.CharField(max_length=100)
    messsage = models.TextField()
    reply =models.CharField(max_length=100,default=False)
    email = models.EmailField()

class Blog(models.Model):
    profile = models.CharField(max_length=100)
    postedDate = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)

    #===== THE RELATIONSHIPS ======#
    comment = models.ForeignKey(BlogComments,related_name='comment',on_delete=models.CASCADE)


    def __str__(self):
        return self.title