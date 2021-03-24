from ninja import Router
from typing import List
from .schemas import ProductsIn, ProductsOut, DepartmentIn, DepartmentOut
from .models import Product, Department
from django.shortcuts import get_object_or_404


router_api = Router()


@router_api.post('/product')
def create_product(request, payload: ProductsIn):
    product = Product.objects.create(**payload.dict())
    return {"id": product.id}


@router_api.post('/department')
def create_department(request, payload: DepartmentIn):
    department = Department.objects.create(**payload.dict())
    return {"id": department.id}


@router_api.get("/product", response=List[ProductsOut])
def list_product(request):
    qs = Product.objects.all()
    return qs


@router_api.get("/department", response=List[DepartmentOut])
def list_department(request):
    qs = Department.objects.all()
    return qs


@router_api.get("/department/{department_id}", response=DepartmentOut)
def get_department(request, department_id: int):
    department = get_object_or_404(Department, id=department_id)
    return department


@router_api.get("/product/{sku}", response=ProductsOut)
def get_product(request, sku: str):
    product = get_object_or_404(Product, sku=sku)
    return product
