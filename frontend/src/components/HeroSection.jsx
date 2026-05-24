import React from 'react';
import { Link } from 'react-router-dom';

function HeroSection() {
  return (
    <section className="relative bg-gradient-to-br from-steel-800 via-steel-700 to-steel-900 text-white overflow-hidden">
      <div className="absolute inset-0 opacity-10">
        <div className="absolute inset-0" style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.4'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
        }} />
      </div>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 md:py-32 relative">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div>
            <div className="inline-flex items-center bg-accent-500/20 text-accent-300 px-4 py-1.5 rounded-full text-sm font-medium mb-6">
              <svg className="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              Supplier Terpercaya Sejak 2010
            </div>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 leading-tight">
              Material <span className="text-accent-400">Baja Ringan</span> & Plafon Berkualitas
            </h1>
            <p className="text-lg text-gray-300 mb-8 max-w-lg">
              Menyediakan rangka baja ringan, plafon PVC, gypsum, spandek, dan aksesoris konstruksi dengan harga pabrik langsung ke proyek Anda.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link to="/products" className="btn-secondary text-center">
                Lihat Katalog Produk
              </Link>
              <Link to="/quotation" className="btn-primary border border-white/20 text-center">
                Minta Penawaran
              </Link>
            </div>
          </div>
          <div className="hidden md:block">
            <div className="relative">
              <div className="bg-steel-600/30 backdrop-blur-sm rounded-2xl p-8 border border-white/10">
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-white/10 rounded-xl p-4 text-center">
                    <p className="text-3xl font-bold text-accent-400">500+</p>
                    <p className="text-sm text-gray-300">Produk Tersedia</p>
                  </div>
                  <div className="bg-white/10 rounded-xl p-4 text-center">
                    <p className="text-3xl font-bold text-accent-400">1000+</p>
                    <p className="text-sm text-gray-300">Proyek Selesai</p>
                  </div>
                  <div className="bg-white/10 rounded-xl p-4 text-center">
                    <p className="text-3xl font-bold text-accent-400">14+</p>
                    <p className="text-sm text-gray-300">Tahun Pengalaman</p>
                  </div>
                  <div className="bg-white/10 rounded-xl p-4 text-center">
                    <p className="text-3xl font-bold text-accent-400">100%</p>
                    <p className="text-sm text-gray-300">Garansi Produk</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default HeroSection;
