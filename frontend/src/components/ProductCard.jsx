import React from 'react';
import { Link } from 'react-router-dom';

function ProductCard({ product }) {
  const formatPrice = (price) => {
    return new Intl.NumberFormat('id-ID', {
      style: 'currency',
      currency: 'IDR',
      minimumFractionDigits: 0,
    }).format(price);
  };

  return (
    <div className="card">
      <div className="h-48 bg-gradient-to-br from-steel-100 to-steel-200 flex items-center justify-center">
        <div className="text-center p-4">
          <svg className="w-16 h-16 text-steel-400 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
          </svg>
          <span className="text-xs text-steel-500 font-medium">{product.category}</span>
        </div>
      </div>
      <div className="p-4">
        <h3 className="font-semibold text-steel-800 text-lg mb-1 line-clamp-1">{product.name}</h3>
        <p className="text-gray-500 text-sm mb-3 line-clamp-2">{product.description}</p>
        <div className="flex items-center justify-between mb-3">
          <div>
            <p className="text-steel-600 font-bold text-lg">{formatPrice(product.price_per_sheet)}</p>
            <p className="text-gray-400 text-xs">per lembar/batang</p>
          </div>
          <span className={`text-xs px-2 py-1 rounded-full ${
            product.stock > 100 ? 'bg-green-100 text-green-700' :
            product.stock > 0 ? 'bg-yellow-100 text-yellow-700' :
            'bg-red-100 text-red-700'
          }`}>
            {product.stock > 100 ? 'Stok Tersedia' :
             product.stock > 0 ? 'Stok Terbatas' : 'Habis'}
          </span>
        </div>
        <div className="text-xs text-gray-400 mb-3 space-y-1">
          <p>Ukuran: {product.width} × {product.length} | Tebal: {product.thickness}</p>
          <p>Material: {product.material} | Warna: {product.color}</p>
        </div>
        <Link
          to={`/products/${product.id}`}
          className="block text-center btn-primary text-sm py-2"
        >
          Lihat Detail
        </Link>
      </div>
    </div>
  );
}

export default ProductCard;
