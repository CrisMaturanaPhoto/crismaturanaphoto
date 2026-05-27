import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  // Dominio canónico real (Vercel resuelve a www). De aquí salen el
  // canonical, el hreflang y las URLs del sitemap, así que debe ser www.
  site: 'https://www.crismaturana.com',
  compressHTML: true,

  // Estaba instalado en package.json pero no registrado: por eso tu
  // sitemap no se regeneraba en cada build. Ahora sí.
  integrations: [sitemap()],

  build: {
    assets: '_assets',
  },
});
