from django.db import models

# Create your models here.
class Asistencia(models.Model):
    full_name = models.CharField(max_length=150)
    id = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    entry_time = models.TimeField()
    exit_time = models.TimeField()
    present = models.BooleanField(default=False)
    observations = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.id} - ${self.observations}"
    
    
    
