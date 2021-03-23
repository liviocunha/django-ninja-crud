from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    sku = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    stock = models.IntegerField
    department = models.ForeignKey(Department, on_delete=models.CASCADE)