from django.db import models

class Hero (models.Model):
    name = models.CharField(max_length=255) #nome do herói
    str = models.IntegerField(null=True) # forca
    dex = models.IntegerField(null=True) # destreza
    con = models.IntegerField(null=True) # constituica
    int = models.IntegerField(null=True) # inteligencia
    wis = models.IntegerField(null=True) # sabedoria
    cha = models.IntegerField(null=True) # carisma
