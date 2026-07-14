/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './core/templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#FAFAFA',
        textMain: '#111111',
        textSecondary: '#666666',
        borderCustom: '#E5E7EB',
        accent: '#2563EB',
        success: '#16A34A',
      },
      fontFamily: {
        satoshi: ['Satoshi', 'Inter', 'sans-serif'],
        inter: ['Inter', 'sans-serif'],
        space: ['Space Grotesk', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
