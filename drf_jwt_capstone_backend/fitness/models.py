from django.db import models

class Fitness(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    age = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    fitness_level = models.CharField(max_length=50, blank=True)
