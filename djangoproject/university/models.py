from django.db import models


class University(models.Model):
    CITY_CHOICES = [
        ('buc', 'Bucharest'),
        ('ias', 'Iași'),
        ('clu', 'Cluj-Napoca'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=3, choices=CITY_CHOICES)

    class Meta:
        verbose_name_plural = 'universities'

    def __str__(self):
        return f'{self.name} ({self.get_city_display()})'

class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_enrolled = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.date_enrolled})'
