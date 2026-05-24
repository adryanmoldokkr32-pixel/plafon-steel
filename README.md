# Plafon Steel

Aplikasi web full-stack untuk supplier material konstruksi baja ringan dan plafon. Menyediakan katalog produk, sistem penawaran harga, dan halaman kontak.

## Tech Stack

- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: React 18, Vite, Tailwind CSS, React Router
- **Data**: JSON file-based storage

## Fitur

- 📦 Katalog produk dengan filter kategori dan pencarian
- 💰 Sistem permintaan penawaran harga (quotation)
- 📱 Responsive design (mobile-first)
- 📞 Halaman kontak dengan formulir pesan
- 📊 Dashboard statistik (admin API)
- 🔗 Integrasi WhatsApp untuk komunikasi cepat

## Struktur Proyek

```
plafon-steel/
├── backend/
│   ├── server.py          # FastAPI application
│   ├── seed_data.py       # Seed database
│   ├── test_server.py     # Backend tests
│   ├── requirements.txt   # Python dependencies
│   └── data/              # JSON data storage
│       ├── products.json
│       ├── quotations.json
│       └── messages.json
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── public/
│   │   └── vite.svg
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── index.css
│       ├── components/
│       │   ├── Navbar.jsx
│       │   ├── Footer.jsx
│       │   ├── HeroSection.jsx
│       │   ├── CategorySection.jsx
│       │   ├── WhyChooseUs.jsx
│       │   └── ProductCard.jsx
│       └── pages/
│           ├── HomePage.jsx
│           ├── ProductsPage.jsx
│           ├── ProductDetailPage.jsx
│           ├── QuotationPage.jsx
│           ├── ContactPage.jsx
│           └── AboutPage.jsx
├── .gitignore
└── README.md
```

## Setup & Run

### Backend

```bash
cd backend
pip install -r requirements.txt
python seed_data.py        # Generate seed data
python -m uvicorn server:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Testing

```bash
cd backend
python -m pytest test_server.py -x -q
```

## API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|----------|
| GET | `/` | Health check |
| GET | `/api/products` | Daftar produk (filter: category, search, min_price, max_price) |
| GET | `/api/products/:id` | Detail produk |
| GET | `/api/categories` | Daftar kategori |
| POST | `/api/quotations` | Buat penawaran baru |
| GET | `/api/quotations` | Daftar penawaran |
| GET | `/api/quotations/:id` | Detail penawaran |
| PUT | `/api/quotations/:id/status` | Update status penawaran |
| POST | `/api/contact` | Kirim pesan kontak |
| GET | `/api/messages` | Daftar pesan |
| GET | `/api/stats` | Statistik dashboard |

## License

MIT
