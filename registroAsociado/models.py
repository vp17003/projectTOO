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
    nombreGenero = models.CharField(max_length=1, choices=GENERO)
        
    class Meta:
        managed = True
        db_table = 'genero'
    def __str__(self):
        return f'{self.idGenero}'

# Tabla tipo documento
class tipoDocumento(models.Model):
    idTipoDocumento = models.AutoField(primary_key=True)
    # Por sno funciona lo de abajo esta la linea 52
    # nombreDocumento = models.CharField(max_length=10, unique=True)
    DOCUMENTO = (
        ('DUI', 'DUI'),
        ('NIT', 'NIT'),
        ('PARTI','PARTIDA DE NACIMIENTO'),
        ('PASAP','PASAPORTE'),
        ('CARNE','CARNE DE RESIDENCIA'),
    )
    nombreDocumento = models.CharField(max_length=6, choices=DOCUMENTO, default='DUI')
        
    class Meta:
        managed = True
        db_table = 'tipoDocumento'
    def __str__(self):
        return f'{self.idTipoDocumento}'

#Tabla actividad economica
class tipoActEconomica(models.Model):
    idTipoActEconomica = models.AutoField(primary_key=True)
    nombreActEconomica= models.CharField(max_length=50)
    rubroActEconomica= models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'tipoActEconomica'
    def __str__(self):
        return f'{self.idTipoActEconomica}'

#Tabla Catalogo de profeciones
class catalogoProfesiones(models.Model):
    idCatalogoProfesiones = models.AutoField(primary_key=True)
    nombreProfesion= models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'catalogoProfesiones'
    def __str__(self):
        return f'{self.idCatalogoProfesiones}'

#Tabla beneficiario
class beneficiario(models.Model):
    idBeneficiario = models.AutoField(primary_key=True)
    nombreBeneficiario= models.CharField(max_length=50)
    apellidoBeneficiario= models.CharField(max_length=50)
    telBeneficiario= models.CharField(max_length=20)
    edadBeneficiario = models.IntegerField()
    PARENTESCO = (
        ('1', 'MAMÁ'),
        ('2', 'PAPÁ'),
        ('3','HERMANO/A'),
        ('4','ABUELA/O'),
        ('5','HIJO/A'),
        ('6','TIO/A'),
        ('7','NIETO/A'),
        ('8','SOBRINO'),
        ('9','PRIMA/O'),
    )
    parenscoBeneficiario = models.CharField(max_length=2, choices=PARENTESCO)
    
    class Meta:
        managed = True
        db_table = 'beneficiario'
    def __str__(self):
        return f'{self.idBeneficiario}'

#Catalogo actividad economica
class catalogoActiEconomica(models.Model):
    idcatalogoActiEconomica = models.AutoField(primary_key=True)
    capacidadPago = models.CharField(max_length=150)

    catalogoProfesiones_idcatalogoProfesiones = models.ForeignKey(catalogoProfesiones, on_delete=models.CASCADE)
    tipoActEconomica_idTipoActEconomica = models.ForeignKey(tipoActEconomica, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'catalogoActiEconomica'
    def __str__(self):
        return f'{self.idcatalogoActiEconomica}'
#Catalogo documentos
class catalogoDocumentos(models.Model):
    idCatalogoDocumentos = models.AutoField(primary_key=True)
    nunDocumento = models.CharField(max_length=50)
    tipoDocumento_idTipoDocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'catalogoDocumentos'
    def __str__(self):
        return f'{self.idCatalogoDocumentos}'
#Cliente        
class cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    primerNombre = models.CharField(max_length=45)
    segundoNombre = models.CharField(max_length=45)
    primerApellido = models.CharField(max_length=45)
    segundoApellido= models.CharField(max_length=45)
    apellidoCasada = models.CharField(max_length=45)
    fechaNacimiento = models.CharField(max_length=11)
    nacionalidad = models.CharField(max_length=45)
    paisNacimiento = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=100)
    subRegion = models.CharField(max_length=50)
    ESTADOCIVIL= (
        ('1', 'CASADO'),
        ('2', 'DIVORCIADO'),
        ('3','VIUDO'),
        ('4','SOLTERO'),
    )
    estadoCivil = models.CharField(max_length=2, choices=ESTADOCIVIL)
    asociacion_idAsociado = models.ForeignKey(asociacion, on_delete=models.CASCADE)
    catalogoDocumentos_idCatalogoDocumento = models.ForeignKey(catalogoDocumentos, on_delete=models.CASCADE)
    genero_idGenero = models.ForeignKey(genero, on_delete=models.CASCADE)
    catalogoActiEconomica_idCatalogoActiEconomica = models.ForeignKey(catalogoActiEconomica, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'cliente'
    def __str__(self):
        return f'{self. idCliente}'

#Catalogo beneficiarios
class catalogoBeneficiario(models.Model):
    idCatalogoBeneficiario = models.AutoField(primary_key=True)
    porcentajeBeneficiario = models.IntegerField()
    beneficiario_idBeneficiario= models.ForeignKey(beneficiario, on_delete=models.CASCADE)
    cliente_idCliente2 = models.ForeignKey(cliente, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'catalogoBeneficiario'
    def __str__(self):
        return f'{self.idCatalogoBeneficiario}'

#Tabla referencias
class referencias(models.Model):
    idReferenciaCliente = models.AutoField(primary_key=True)
    nombreReferencia = models.CharField(max_length=100)
    telReferencia = models.CharField(max_length=20)
    correoReferencia = models.CharField(max_length=100)
    cliente_idCliente3 = models.ForeignKey(cliente, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'referencias'
    def __str__(self):
        return f'{self.idReferenciaCliente}'

#Catalogo referencia
class catalogoReferencias(models.Model):
    idCatalogoReferencia = models.AutoField(primary_key=True)
    TIPOREFERENCIA = (
        ('1', 'PERSONAL'),
        ('2', 'FAMILIAR'),
    )
    parenscoBeneficiario = models.CharField(max_length=2, choices=TIPOREFERENCIA)
    asociaciones = models.CharField(max_length=120)
    cliente_idCliente1 = models.ForeignKey(cliente, on_delete=models.CASCADE)
    referencias_idReferenciaCliente = models.ForeignKey(referencias, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'catalogoReferencias'
    def __str__(self):
        return f'{self.idCatalogoReferencia}'