import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://www.crismaturana.com',
  compressHTML: true,
  build: {
    assets: '_assets',
  },
});
