from ninja import schema


class ProductsIn(schema):
    sku: str
    title: str
    stock: int = 0
    department_id: int = None


class ProductsOut(schema):
    id: int
    sku: str
    title: str
    stock: int = 0
    department_id: int = None
