from django.db import models

class A(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()

class B(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    a = models.ForeignKey('A')

