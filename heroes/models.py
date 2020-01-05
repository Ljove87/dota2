from django.db import models


class Hero(models.Model):
    class Meta:
        verbose_name_plural = "Heroes"

    AGILITY = "AGI"
    INTELLECT = 'INT'
    STRENGTH = 'STR'
    HERO_CHOICES = [
        (AGILITY, 'Agility'),
        (INTELLECT, 'Intellect'),
        (STRENGTH, 'Strength'),
    ]
    name = models.CharField(max_length=100)
    hero_type = models.CharField(max_length=20, choices=HERO_CHOICES, default=AGILITY)

    def __str__(self):
        return self.name
