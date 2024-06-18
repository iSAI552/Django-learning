from django.db import models
from django.utils import timezone


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
