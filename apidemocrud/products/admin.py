from django.contrib import admin
from .models import Department, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'title', 'stock', 'department')
    search_fields = ('sku', 'title')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Product, ProductAdmin)
