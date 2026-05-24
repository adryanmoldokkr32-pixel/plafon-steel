import pytest
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Plafon Steel API"
    assert data["version"] == "1.0.0"
    assert data["status"] == "active"


def test_get_products():
    response = client.get("/api/products")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0


def test_get_products_by_category():
    response = client.get("/api/products?category=Plafon PVC")
    assert response.status_code == 200
    products = response.json()
    assert all(p["category"] == "Plafon PVC" for p in products)


def test_get_products_search():
    response = client.get("/api/products?search=baja")
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0


def test_get_product_by_id():
    all_products = client.get("/api/products").json()
    product_id = all_products[0]["id"]
    response = client.get(f"/api/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id


def test_get_product_not_found():
    response = client.get("/api/products/nonexistent-id")
    assert response.status_code == 404


def test_get_categories():
    response = client.get("/api/categories")
    assert response.status_code == 200
    data = response.json()
    assert "categories" in data
    assert len(data["categories"]) > 0


def test_create_quotation():
    products = client.get("/api/products").json()
    product = products[0]
    payload = {
        "customer_name": "Budi Santoso",
        "customer_phone": "081234567890",
        "customer_email": "budi@example.com",
        "customer_address": "Jl. Merdeka No. 10, Jakarta",
        "project_name": "Renovasi Rumah",
        "items": [
            {
                "product_id": product["id"],
                "product_name": product["name"],
                "quantity": 10,
                "unit": "lembar",
                "price": product["price_per_sheet"],
                "subtotal": product["price_per_sheet"] * 10,
            }
        ],
        "notes": "Kirim pagi hari",
    }
    response = client.post("/api/quotations", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Budi Santoso"
    assert data["status"] == "pending"
    assert data["total"] == product["price_per_sheet"] * 10


def test_get_quotations():
    response = client.get("/api/quotations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_submit_contact():
    payload = {
        "name": "Andi",
        "email": "andi@example.com",
        "phone": "087654321098",
        "subject": "Tanya harga",
        "message": "Saya ingin tahu harga plafon PVC untuk area 50m2",
    }
    response = client.post("/api/contact", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Pesan berhasil dikirim"


def test_get_messages():
    response = client.get("/api/messages")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_stats():
    response = client.get("/api/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_products" in data
    assert "total_quotations" in data
    assert "pending_quotations" in data
    assert "total_messages" in data


def test_price_filter():
    response = client.get("/api/products?min_price=100000&max_price=150000")
    assert response.status_code == 200
    products = response.json()
    for p in products:
        assert p["price_per_sheet"] >= 100000
        assert p["price_per_sheet"] <= 150000
