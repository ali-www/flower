from django.db import models
from django.contrib.auth.models import User
from flower.models import PostFlower


class Action(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    flower = models.ForeignKey(to=PostFlower, on_delete=models.CASCADE, related_name='actions')
    liked = models.BooleanField(null=True)

    class Meta:
        unique_together = ['user', 'flower']

    def __str__(self):
        return str(self.flower)    
