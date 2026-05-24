/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        steel: {
          50: '#f4f7fa',
          100: '#e8eef4',
          200: '#c5d6e7',
          300: '#a2beda',
          400: '#5c8ec0',
          500: '#1565a6',
          600: '#135b95',
          700: '#104c7d',
          800: '#0c3d64',
          900: '#0a3252',
        },
        accent: {
          50: '#fff8e1',
          100: '#ffecb3',
          200: '#ffe082',
          300: '#ffd54f',
          400: '#ffca28',
          500: '#ffc107',
          600: '#ffb300',
          700: '#ffa000',
          800: '#ff8f00',
          900: '#ff6f00',
        }
      }
    },
  },
  plugins: [],
}
