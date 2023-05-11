from django.db import models

class DetalheCurso (models.Model):
    Curso = models.CharField (max_length=100)
    Turma= models.CharField (max_length=100)
# Create your models here.
