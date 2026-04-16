from django.db import models

# Create your models here.
class Asistencia(models.Model):
    Nombre = models.CharField(max_length=150)
    id = models.CharField(max_length=20, primary_key=True)
    corero = models.EmailField()
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    presente = models.BooleanField(default=False)
    observationes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.Nombre} - {self.id} - {self.observationes}'

