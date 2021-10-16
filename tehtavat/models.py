from django.db import models


# Create your models here.
class TehtavaRyhma(models.Model):
    nimi = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nimi


class Tehtava(models.Model):
    nimi = models.CharField(max_length=100, default="")
    maxpisteet = models.IntegerField()
    suoritusaika = models.TimeField(null=True, blank=True)
    ajanylitys = models.TimeField(null=True, blank=True)
    ryhma = models.OneToOneField(TehtavaRyhma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nimi
