from products.models import Product, Department
from django.test import Client
import pytest


@pytest.mark.django_db
def test_with_client(client: Client):
    assert Department.objects.count() == 0
    test_item = {"title": "Department Test"}
    response = client.post("/api/department", **json_payload(test_item))
    assert response.status_code == 200
    assert Department.objects.count() == 1

    assert Product.objects.count() == 0
    test_item = {"sku": "111test", "title": "Product Test", "stock": 1, "department_id": 1}
    response = client.post("/api/product", **json_payload(test_item))
    assert response.status_code == 200
    assert Department.objects.count() == 1


def json_payload(data):
    import json

    return dict(data=json.dumps(data), content_type="application/json")