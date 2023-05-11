from django.db import models

class Turma (models.Model):
    Codigo = models.CharField (max_length=100)
    Curso = models.CharField (max_length=100)
# Create your models here.
