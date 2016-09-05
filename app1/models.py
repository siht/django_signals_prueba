from django.db import models

class A(models.Model):
    nombre = models.TextField()

class B(models.Model):
    nombre = models.TextField()
    a = models.ForeignKey('A')
