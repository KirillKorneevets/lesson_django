from django.db import models



class Posts(models.Model):
    title =  models.CharField(max_length=100)
    text = models.TextField()
    counter = models.PositiveIntegerField()

class User(models.Model):
    username =  models.CharField(max_length=100)
    age = models.PositiveIntegerField()