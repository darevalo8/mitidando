from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    country = models.CharField('País', max_length=50)

    def __str__(self):
        return self.country


class Deparment(models.Model):
    deparment_name = models.CharField('Departamento', max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.deparment_name


class City(models.Model):
    city_name = models.CharField('Ciudad', max_length=50)
    deparment = models.ForeignKey(Deparment, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document = models.CharField("Documento", max_length=12)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
