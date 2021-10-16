from django.db import models
from tehtavat.models import Tehtava


# Create your models here.
class Rasti(models.Model):
    name = models.CharField(max_length=100, default="")
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class ReittiPiste(models.Model):
    numero = models.IntegerField()
    rasti = models.OneToOneField(Rasti)
    tehtavat = models.ManyToManyField(Tehtava, blank=True)

    def __str__(self):
        return self.numero


class Reitti(models.Model):
    nimi = models.CharField(max_length=100, default="")
    reittipisteet = models.ManyToManyField(ReittiPiste, blank=True)

    def __str__(self):
        return self.nimi


class Sarja(models.Model):
    nimi = models.CharField(max_length=100, default="")
    reitit = models.ManyToManyField(Reitti, on_delete=models.CASCADE)

    def __str__(self):
        return self.nimi


class Vartio(models.Model):
    nimi = models.CharField(max_length=100, default="")
    lippukunta = models.CharField(max_length=250, default="")
    johtaja = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.nimi

