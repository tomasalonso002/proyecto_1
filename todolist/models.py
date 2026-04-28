from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre


# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    completada = models.BooleanField(default=False, help_text="¿La tarea esta completada?")
    fecha_completado = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responsable", default= None, blank=True, null= True)
    etiqueta = models.ManyToManyField(Etiqueta, default=None, blank= True, null= True, related_name="etiqueta")
    activo = models.BooleanField(default=True, help_text='Verdadero sino esta archivado')
    
    def __str__(self):
        return f"Soy la tarea: {self.nombre} {self.etiqueta}"