from datetime import datetime, timezone
from django.db import models

# Create your models here.
class CrearTarea(models.Model):
    titulo_tarea = models.CharField(max_length=100)
    descrip_tarea = models.CharField(max_length=250)
    fechaLim_tarea = models.DateField('Fecha de publicacion')
    
    def __str__(self):
        return self.titulo_tarea
      
    def was_published_recently(self):
        return self.fechaLim_tarea >= timezone.now() - datetime.timedelta(days=1)