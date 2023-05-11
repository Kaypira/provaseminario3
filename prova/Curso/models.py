from django.db import models

class Curso (models.Model):
    codigo = models.CharField (max_length=100)
    Turma = models.CharField (max_length=100)
# Create your models here.
