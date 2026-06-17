# Cristóbal Maturana – Astro Site

A faithful recreation of [crismaturana.com](https://crismaturana.com/) built with Astro 4.

## Getting Started

```bash
# Install dependencies
npm install

# Start dev server (localhost:4321)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
src/
├── layouts/
│   └── Layout.astro          # Global layout with nav, footer, lightbox
├── components/
│   ├── Nav.astro             # Responsive sticky navigation
│   ├── Footer.astro          # Footer with awards & social links
│   └── Gallery.astro         # Reusable gallery (masonry / grid / justified)
└── pages/
    ├── index.astro            # Homepage with hero slider
    ├── about-me.astro
    ├── prices.astro
    ├── faq.astro
    ├── contact.astro
    └── portfolio/
        ├── index.astro
        ├── portraits.astro
        ├── weddings.astro
        ├── travel-culture.astro
        ├── aerial.astro
        ├── landscapes.astro
        ├── architecture.astro
        ├── night-sky.astro
        └── photo-tours-vietnam-2026.astro
```

## Features

- **Zero JS framework** – Pure Astro with vanilla JS only where needed
- **Hero slider** – Auto-playing with keyboard and dot navigation
- **Lightbox** – Click any gallery image to view full size with arrow navigation
- **Masonry & grid galleries** – Multiple layout modes per portfolio category
- **Mobile responsive** – Hamburger nav, stacked layouts on small screens
- **Dark theme** – Deep charcoal palette with warm gold accents
- **Google Fonts** – Playfair Display (serif) + Lato (sans)
- **Optimised images** – `loading="lazy"` and `decoding="async"` on all gallery images

## Deployment

Deploy to any static host (Vercel, Netlify, Cloudflare Pages):

```bash
npm run build
# Upload the `dist/` folder
```
