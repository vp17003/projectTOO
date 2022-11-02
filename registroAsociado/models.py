from dataclasses import asdict
from django.db import models


# Create your models here.
class ejecutivo(models.Model):
    idEjecutivo = models.AutoField(primary_key=True)
    nombreEjecutivo = models.CharField(max_length=50)
    apellidoEjecutivo = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'ejecutivo'
    def __str__(self):
        return f'{self.idEjecutivo}'

# Create your models here.
class asociacion(models.Model):
    idAsociado = models.AutoField(primary_key=True)
    fechaAsociacion = models.CharField(max_length=50)
    lugarAsociacion = models.CharField(max_length=100)
    ejecutivo_idEjecutivo= models.ForeignKey(ejecutivo, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'asociacion'
    def __str__(self):
        return f'{self.idAsociado}'