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


@router_api.put("/department/{department_id}")
def update_department(request, department_id: int, payload: DepartmentIn):
    department = get_object_or_404(Department, id=department_id)
    for attr, value in payload.dict().items():
        setattr(department, attr, value)
    department.save()
    return {"success": True}


@router_api.put("/product/{sku}")
def update_product(request, sku: str, payload: ProductsIn):
    product = get_object_or_404(Product, sku=sku)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@router_api.delete("/department/{department_id}")
def delete_department(request, department_id: int):
    department = get_object_or_404(Department, id=department_id)
    department.delete()
    return {"success": True}


@router_api.delete("/product/{sku}")
def delete_product(request, sku: str):
    product = get_object_or_404(Product, sku=sku)
    product.delete()
    return {"success": True}



