from django.contrib import admin
from .models import Department, Product, Client


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'title', 'stock', 'department')
    search_fields = ('sku', 'title')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
