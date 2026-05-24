from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import json
import os
import uuid

app = FastAPI(title="Plafon Steel API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def load_json(filename: str):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_json(filename: str, data):
    filepath = os.path.join(DATA_DIR, filename)
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Models
class Product(BaseModel):
    id: Optional[str] = None
    name: str
    category: str
    description: str
    thickness: str
    width: str
    length: str
    price_per_meter: float
    price_per_sheet: float
    stock: int
    image_url: Optional[str] = ""
    material: str = "Baja Ringan"
    color: str = "Silver"
    weight_per_meter: Optional[float] = None
    created_at: Optional[str] = None


class QuotationItem(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    unit: str = "lembar"
    price: float
    subtotal: float


class QuotationRequest(BaseModel):
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = ""
    customer_address: str
    project_name: Optional[str] = ""
    items: List[QuotationItem]
    notes: Optional[str] = ""


class Quotation(BaseModel):
    id: Optional[str] = None
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = ""
    customer_address: str
    project_name: Optional[str] = ""
    items: List[QuotationItem]
    total: float
    notes: Optional[str] = ""
    status: str = "pending"
    created_at: Optional[str] = None


class ContactMessage(BaseModel):
    name: str
    email: str
    phone: Optional[str] = ""
    subject: str
    message: str


# Routes
@app.get("/")
def root():
    return {"message": "Plafon Steel API", "version": "1.0.0", "status": "active"}


@app.get("/api/products", response_model=List[Product])
def get_products(
    category: Optional[str] = None,
    search: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
):
    products = load_json("products.json")
    if category:
        products = [p for p in products if p["category"].lower() == category.lower()]
    if search:
        search_lower = search.lower()
        products = [
            p for p in products
            if search_lower in p["name"].lower()
            or search_lower in p["description"].lower()
        ]
    if min_price is not None:
        products = [p for p in products if p["price_per_sheet"] >= min_price]
    if max_price is not None:
        products = [p for p in products if p["price_per_sheet"] <= max_price]
    return products


@app.get("/api/products/{product_id}")
def get_product(product_id: str):
    products = load_json("products.json")
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
    return product


@app.get("/api/categories")
def get_categories():
    products = load_json("products.json")
    categories = list(set(p["category"] for p in products))
    return {"categories": sorted(categories)}


@app.post("/api/quotations", response_model=Quotation)
def create_quotation(request: QuotationRequest):
    quotations = load_json("quotations.json")
    total = sum(item.subtotal for item in request.items)
    quotation = Quotation(
        id=str(uuid.uuid4()),
        customer_name=request.customer_name,
        customer_phone=request.customer_phone,
        customer_email=request.customer_email,
        customer_address=request.customer_address,
        project_name=request.project_name,
        items=request.items,
        total=total,
        notes=request.notes,
        status="pending",
        created_at=datetime.now().isoformat(),
    )
    quotations.append(quotation.model_dump())
    save_json("quotations.json", quotations)
    return quotation


@app.get("/api/quotations")
def get_quotations(status: Optional[str] = None):
    quotations = load_json("quotations.json")
    if status:
        quotations = [q for q in quotations if q["status"] == status]
    return quotations


@app.get("/api/quotations/{quotation_id}")
def get_quotation(quotation_id: str):
    quotations = load_json("quotations.json")
    quotation = next((q for q in quotations if q["id"] == quotation_id), None)
    if not quotation:
        raise HTTPException(status_code=404, detail="Penawaran tidak ditemukan")
    return quotation


@app.put("/api/quotations/{quotation_id}/status")
def update_quotation_status(quotation_id: str, status: str = Query(...)):
    quotations = load_json("quotations.json")
    for q in quotations:
        if q["id"] == quotation_id:
            q["status"] = status
            save_json("quotations.json", quotations)
            return q
    raise HTTPException(status_code=404, detail="Penawaran tidak ditemukan")


@app.post("/api/contact")
def submit_contact(message: ContactMessage):
    messages = load_json("messages.json")
    msg_data = message.model_dump()
    msg_data["id"] = str(uuid.uuid4())
    msg_data["created_at"] = datetime.now().isoformat()
    msg_data["read"] = False
    messages.append(msg_data)
    save_json("messages.json", messages)
    return {"message": "Pesan berhasil dikirim", "id": msg_data["id"]}


@app.get("/api/messages")
def get_messages():
    return load_json("messages.json")


@app.get("/api/stats")
def get_stats():
    products = load_json("products.json")
    quotations = load_json("quotations.json")
    messages = load_json("messages.json")
    return {
        "total_products": len(products),
        "total_quotations": len(quotations),
        "pending_quotations": len([q for q in quotations if q["status"] == "pending"]),
        "total_messages": len(messages),
        "unread_messages": len([m for m in messages if not m.get("read", False)]),
        "total_revenue": sum(q.get("total", 0) for q in quotations if q.get("status") == "approved"),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
