from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=100, help_text='Departamento do produto.',
                             verbose_name='DEPARTAMENTO DO PRODUTO')

    def __str__(self):
        return self.title


class Product(models.Model):
    sku = models.CharField(max_length=100, help_text='Código SKU do produto.', verbose_name='SKU DO PRODUTO')
    title = models.CharField(max_length=100, help_text='Nome do produto.', verbose_name='NOME DO PRODUTO')
    stock = models.IntegerField(help_text='Estoque do produto', verbose_name='ESTOQUE')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.sku
