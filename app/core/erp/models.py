from django.db import models
from datetime import datetime

# Create your models here.


class Client(models.Model):
    names = models.CharField(verbose_name='Nombres', max_length=100)
    last_names = models.CharField(verbose_name='Apellidos', max_length=100)
    dni = models.CharField(verbose_name='Dni', unique=True, max_length=10)
    birth_date = models.DateField(verbose_name='Fecha nacimiento', default=datetime.now)
    address = models.CharField(verbose_name='Direccion', max_length=150)
    gender = models.CharField(verbose_name='Sexo', max_length=50)

    def __str__(self):
        return self.names, self.last_names, self.dni

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    client = models.ForeignKey(Client, verbose_name='Cliente', on_delete=models.CASCADE)
    sale_date = models.DateField(verbose_name='Fecha de la venta', default=datetime.now)
    subtotal = models.DecimalField(max_digits=2, max_length=9, decimal_places=2)
    iva = models.DecimalField(max_digits=2, max_length=2, default=0.00, decimal_places=2)
    total = models.DecimalField(max_digits=2, max_length=9, decimal_places=2)

    def __str__(self):
        return self.client, self.sale_date, self.total

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(verbose_name='Nombre', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nombre', unique=True, max_length=100)
    image = models.ImageField(upload_to='product/%Y/%m/%d', verbose_name='Imagen')
    pvp = models.CharField(verbose_name='PvP', max_length=150)

    def __str__(self):
        return self.name, self.category

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, verbose_name='Venta', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Producto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    price = models.DecimalField(verbose_name='Precio', max_length=9, max_digits=2, decimal_places=2)
    subtotal = models.DecimalField(max_digits=2, max_length=9, decimal_places=2)

    def __str__(self):
        return self.sale, self.product, self.quantity, self.subtotal

    class Meta:
        verbose_name = 'Detalle venta'
        verbose_name_plural = 'Detalle ventas'
        ordering = ['id']
