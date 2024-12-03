from django.db import models


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    balance = models.DecimalField(decimal_places=2, max_digits=99, default=0.00)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=99, default=1000)
    size = models.DecimalField(decimal_places=2, max_digits=99)
    description = models.TextField(default='Very good game, bro!')
    age_limited = models.PositiveIntegerField(default=18)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

