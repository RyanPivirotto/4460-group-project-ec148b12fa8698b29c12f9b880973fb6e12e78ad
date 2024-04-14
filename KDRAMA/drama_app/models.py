from django.db import models
from django.core.validators import MaxValueValidator

class User(models.Model):
    user_id = models.AutoField(primary_key=True, null=False, validators=[MaxValueValidator(99999999999)])
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)

class Award(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Character(models.Model):
    name = models.CharField(max_length=100)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Drama(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    seasons = models.IntegerField()
    characters = models.ManyToManyField(Character)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title
