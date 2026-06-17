import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://crismaturana.com',
  compressHTML: true,
  build: {
    assets: '_assets',
  },
});
