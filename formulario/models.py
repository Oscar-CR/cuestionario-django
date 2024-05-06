from django.db import models

class Cuestionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    periodo = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    ultimaActualizacion = models.DateTimeField(auto_now=True)

class Pregunta(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipoPregunta = models.ForeignKey('TipoPregunta', on_delete=models.CASCADE)
    descripcion = models.TextField()
    opciones = models.TextField()
    respuesta = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

class TipoPregunta(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

class CuestionarioPregunta(models.Model):
    id = models.BigAutoField(primary_key=True)
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

class Respuesta(models.Model):
    id = models.BigAutoField(primary_key=True)
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    ultimaActualizacion = models.DateTimeField(auto_now=True)