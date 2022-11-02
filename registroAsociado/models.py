from dataclasses import asdict
from django.db import models


# Create your models here.
# Tabla ejecutico
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
#Tabla asociacion
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

#Tabla genero
class genero(models.Model):
    idGenero = models.AutoField(primary_key=True)
    # Por sno funciona lo de abajo esta la linea 36
    # nombreGenero = models.CharField(max_length=8, unique=True)
    GENERO = (
        ('H', 'HOMBRE'),
        ('M', 'MUJER'),
    )
    estadoCuenta = models.CharField(max_length=1, choices=GENERO)
        
    class Meta:
        managed = True
        db_table = 'genero'
    def __str__(self):
        return f'{self.idGenero}'

class tipoDocumento(models.Model):
    idTipoDocumento = models.AutoField(primary_key=True)
    # Por sno funciona lo de abajo esta la linea 52
    # nombreGDocumento = models.CharField(max_length=10, unique=True)
    DOCUMENTO = (
        ('DUI', 'DUI'),
        ('NIT', 'NIT'),
        ('PARTI','PARTIDA DE NACIMIENTO'),
        ('PASAP','PASAPORTE'),
        ('CARNE','CARNE DE RESIDENCIA'),
    )
    nombreDocumento = models.CharField(max_length=5, choices=DOCUMENTO, default='DUI')
        
    class Meta:
        managed = True
        db_table = 'tipoDocumento'
    def __str__(self):
        return f'{self.idTipoDocumento}'

    