from django.db import models
from datetime import datetime


# Create your models here.


class AnimalType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=50)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=datetime.now, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Exhibition(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    fund = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Reward(models.Model):
    PLACE = [
        ('1', 'Победитель'),
        ('2', 'Топ-2'),
        ('3', 'Топ-3'),
        ('4', 'Топ-4'),
        ('5', 'Участник'),
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    place = models.CharField(max_length=1, choices=PLACE)
    prize = models.PositiveBigIntegerField()
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)

