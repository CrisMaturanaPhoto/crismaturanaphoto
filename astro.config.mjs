import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.crismaturana.com',
  compressHTML: true,
  build: {
    assets: '_assets',
  },
  integrations: [sitemap()],
});
