from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=150)
    system = models.CharField(max_length=150)
    players = models.SmallIntegerField(max_length=3)
    archived = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)
    rating = models.SmallIntegerField(max_length=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)