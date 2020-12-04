from django.db import models

# Create your models here.

class PostFlower(models.Model):
   
    title = models.CharField(max_length=100)
    #title_ar = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    def __str__(self):
        return self.title