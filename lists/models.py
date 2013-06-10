from django.db import models

class List(models.Model):
    name = models.TextField()

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List)
