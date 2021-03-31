from ninja import Schema


class DepartmentIn(Schema):
    title: str


class DepartmentOut(Schema):
    id: int
    title: str


class ProductsIn(Schema):
    sku: str
    title: str
    stock: int = 0
    department_id: int = None


class ProductsOut(Schema):
    id: int
    sku: str
    title: str
    stock: int = 0
    department: DepartmentOut = None
