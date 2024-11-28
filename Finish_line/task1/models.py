from django.db import models


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=99)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=99)
    size = models.DecimalField(decimal_places=2, max_digits=99)
    description = models.TextField()
    age_limited = models.BooleanField(default=None)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

