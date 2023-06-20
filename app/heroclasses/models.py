from django.db import models

class Heroclass (models.Model):
    heroclass = models.CharField(max_length=255) #nome do herói