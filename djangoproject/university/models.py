from django.db import models


class University(models.Model):
    CITY_CHOICES = [
        ('buc', 'Bucharest'),
        ('ias', 'Iași'),
        ('clu', 'Cluj-Napoca'),
    ]
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=3, choices=CITY_CHOICES)


class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_enrolled = models.DateField()
