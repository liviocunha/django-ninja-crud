from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from apidemocrud.products.api import router_api as apidemocrud_router


api = NinjaAPI(
    version='1.0',
    csrf=True,
    title='API Demo CRUD',
    description='CRUD - Create, Retrieve, Update, Delete are the four basic functions of persistent storage.\n'
                'https://github.com/liviocunha/django-ninja-crud',
    urls_namespace='public_api',
)
api.add_router('/crud/', apidemocrud_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
