from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class HeroVariety(models.Model):
    HEROES_TYPE_CHOICE = [
        ('IM', 'Iron Man'),
        ('CA', 'Captain America'),
        ('BM', 'Batman'),
        ('HK', 'Hulk')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="heroes/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=HEROES_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


#    One-to-Many relations
class HeroReview(models.Model):
    hero = models.ForeignKey(HeroVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.hero.name}"


# Many-to-Many relations

class CountryPopularIn(models.Model):
    CONTINENT_TYPE_CHOICES = [
        ("AS", "Asia"),
        ("EU", "Europe"),
        ("AF", "Africa"),
        ("SA", "South America"),
        ("NA", "North America"),
        ("AT", "Antarctica"),
        ("AU", "Australia")
    ]
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=2, choices=CONTINENT_TYPE_CHOICES)
    heroes_popular = models.ManyToManyField(HeroVariety, related_name="countries")

    def __str__(self):
        return self.name


# One-to-One Relationship
class SpecialPower(models.Model):
    hero = models.OneToOneField(HeroVariety, on_delete=models.CASCADE, related_name='superPower')
    power_strength = models.CharField(max_length=100)

    def __str__(self):
        return f"SpecialPower of {self.hero.name}"
