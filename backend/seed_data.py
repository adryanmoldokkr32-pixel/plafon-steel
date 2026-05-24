import json
import os
import uuid

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

products = [
    {
        "id": str(uuid.uuid4()),
        "name": "Plafon PVC Putih Polos",
        "category": "Plafon PVC",
        "description": "Plafon PVC berkualitas tinggi dengan permukaan halus dan tahan air. Cocok untuk rumah tinggal dan kantor.",
        "thickness": "8mm",
        "width": "20cm",
        "length": "400cm",
        "price_per_meter": 25000,
        "price_per_sheet": 100000,
        "stock": 500,
        "image_url": "/images/plafon-pvc-putih.jpg",
        "material": "PVC",
        "color": "Putih",
        "weight_per_meter": 1.2,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Plafon PVC Motif Kayu",
        "category": "Plafon PVC",
        "description": "Plafon PVC dengan motif serat kayu natural. Memberikan kesan hangat dan elegan pada ruangan.",
        "thickness": "8mm",
        "width": "20cm",
        "length": "400cm",
        "price_per_meter": 35000,
        "price_per_sheet": 140000,
        "stock": 300,
        "image_url": "/images/plafon-pvc-kayu.jpg",
        "material": "PVC",
        "color": "Coklat Kayu",
        "weight_per_meter": 1.3,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Rangka Baja Ringan C75",
        "category": "Rangka Baja Ringan",
        "description": "Rangka baja ringan profil C75 dengan ketebalan 0.75mm. Ideal untuk rangka atap dan plafon.",
        "thickness": "0.75mm",
        "width": "75mm",
        "length": "600cm",
        "price_per_meter": 18000,
        "price_per_sheet": 108000,
        "stock": 800,
        "image_url": "/images/baja-c75.jpg",
        "material": "Baja Ringan",
        "color": "Silver",
        "weight_per_meter": 0.85,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Rangka Baja Ringan C100",
        "category": "Rangka Baja Ringan",
        "description": "Rangka baja ringan profil C100 untuk konstruksi atap bentang lebar. Kekuatan tinggi dan ringan.",
        "thickness": "1.0mm",
        "width": "100mm",
        "length": "600cm",
        "price_per_meter": 28000,
        "price_per_sheet": 168000,
        "stock": 600,
        "image_url": "/images/baja-c100.jpg",
        "material": "Baja Ringan",
        "color": "Silver",
        "weight_per_meter": 1.2,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Hollow Galvalum 20x40",
        "category": "Hollow & Aksesoris",
        "description": "Hollow galvalum ukuran 20x40mm untuk rangka plafon. Anti karat dan tahan lama.",
        "thickness": "0.3mm",
        "width": "20mm",
        "length": "400cm",
        "price_per_meter": 12000,
        "price_per_sheet": 48000,
        "stock": 1000,
        "image_url": "/images/hollow-20x40.jpg",
        "material": "Galvalum",
        "color": "Silver",
        "weight_per_meter": 0.5,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Hollow Galvalum 40x40",
        "category": "Hollow & Aksesoris",
        "description": "Hollow galvalum ukuran 40x40mm untuk rangka plafon heavy duty. Kokoh dan presisi.",
        "thickness": "0.4mm",
        "width": "40mm",
        "length": "400cm",
        "price_per_meter": 18000,
        "price_per_sheet": 72000,
        "stock": 750,
        "image_url": "/images/hollow-40x40.jpg",
        "material": "Galvalum",
        "color": "Silver",
        "weight_per_meter": 0.75,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Spandek Galvalum 0.3mm",
        "category": "Atap & Spandek",
        "description": "Atap spandek galvalum gelombang dengan ketebalan 0.3mm. Ringan dan mudah dipasang.",
        "thickness": "0.3mm",
        "width": "100cm",
        "length": "300cm",
        "price_per_meter": 45000,
        "price_per_sheet": 135000,
        "stock": 400,
        "image_url": "/images/spandek-03.jpg",
        "material": "Galvalum",
        "color": "Silver",
        "weight_per_meter": 2.5,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Spandek Warna 0.35mm",
        "category": "Atap & Spandek",
        "description": "Atap spandek berwarna dengan lapisan cat khusus. Tersedia dalam berbagai pilihan warna.",
        "thickness": "0.35mm",
        "width": "100cm",
        "length": "300cm",
        "price_per_meter": 55000,
        "price_per_sheet": 165000,
        "stock": 350,
        "image_url": "/images/spandek-warna.jpg",
        "material": "Galvalum",
        "color": "Merah",
        "weight_per_meter": 2.8,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Sekrup Baja Ringan 12x20",
        "category": "Hollow & Aksesoris",
        "description": "Sekrup self drilling untuk baja ringan. 1 dus isi 1000 pcs.",
        "thickness": "12gauge",
        "width": "20mm",
        "length": "20mm",
        "price_per_meter": 0,
        "price_per_sheet": 150000,
        "stock": 200,
        "image_url": "/images/sekrup-12x20.jpg",
        "material": "Stainless Steel",
        "color": "Silver",
        "weight_per_meter": None,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Plafon Kalsiboard 3.5mm",
        "category": "Plafon Kalsiboard",
        "description": "Plafon kalsiboard serat semen berkualitas. Tahan api dan anti rayap.",
        "thickness": "3.5mm",
        "width": "120cm",
        "length": "240cm",
        "price_per_meter": 30000,
        "price_per_sheet": 85000,
        "stock": 450,
        "image_url": "/images/kalsiboard-35.jpg",
        "material": "Kalsiboard",
        "color": "Abu-abu",
        "weight_per_meter": 3.5,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Plafon Gypsum 9mm",
        "category": "Plafon Gypsum",
        "description": "Plafon gypsum standar 9mm untuk interior. Permukaan rata dan mudah di finishing.",
        "thickness": "9mm",
        "width": "120cm",
        "length": "240cm",
        "price_per_meter": 25000,
        "price_per_sheet": 72000,
        "stock": 600,
        "image_url": "/images/gypsum-9mm.jpg",
        "material": "Gypsum",
        "color": "Putih",
        "weight_per_meter": 6.5,
        "created_at": "2024-01-15T08:00:00"
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Kawat Baja 1.2mm",
        "category": "Hollow & Aksesoris",
        "description": "Kawat baja galvanis untuk pengikat rangka. 1 roll = 50 meter.",
        "thickness": "1.2mm",
        "width": "1.2mm",
        "length": "5000cm",
        "price_per_meter": 500,
        "price_per_sheet": 25000,
        "stock": 150,
        "image_url": "/images/kawat-baja.jpg",
        "material": "Baja Galvanis",
        "color": "Silver",
        "weight_per_meter": 0.01,
        "created_at": "2024-01-15T08:00:00"
    },
]

quotations = []
messages = []

with open(os.path.join(DATA_DIR, "products.json"), "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

with open(os.path.join(DATA_DIR, "quotations.json"), "w", encoding="utf-8") as f:
    json.dump(quotations, f, indent=2, ensure_ascii=False)

with open(os.path.join(DATA_DIR, "messages.json"), "w", encoding="utf-8") as f:
    json.dump(messages, f, indent=2, ensure_ascii=False)

print(f"Seeded {len(products)} products")
print(f"Data directory: {DATA_DIR}")
print("Done!")
