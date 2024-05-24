from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen',null=True)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    
class roles(models.Model):
    tipo = models.CharField(max_length=100)
    usuarios = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.tipo} - {self.usuarios}"
    
class imagen(models.Model):
    imagen = models.ImageField(upload_to='images/')
    
class categoria(models.Model):
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.tipo}"
    

def validate_positive_number(value):
    if value <= 0:
        raise ValidationError("El valor debe ser un número positivo.")
    
class producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(validators=[validate_positive_number])
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    imagen = models.ForeignKey(imagen, on_delete=models.CASCADE) 
    def __str__(self):
        return f"{self.titulo} - {self.estado}"

class oferta(models.Model):
    usuarios = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.usuarios} - {self.producto}"
    
class favorito(models.Model):
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.usuarios} - {self.producto} - {self.categoria}"
    
class transaccion(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    detalles = models.CharField(max_length=100)
    usuarios = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.usuarios} - {self.detalles} - {self.fecha_hora}"

class historial(models.Model):
    fecha_compra = models.DateTimeField(auto_now_add=True)
    transaccion = models.ForeignKey(transaccion, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.transaccion} - {self.fecha_compra}"