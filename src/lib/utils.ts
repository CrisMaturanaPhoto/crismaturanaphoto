// utils.ts — Helpers compartidos por las páginas de la home (EN/ES).
import { getCollection } from 'astro:content';

/** Devuelve los `limit` posts de blog más recientes, ordenados desc por fecha. */
export async function getLatestBlogPosts(limit = 3) {
  const posts = await getCollection('blog');
  return posts
    .sort(
      (a, b) =>
        b.data.publishDate.getTime() - a.data.publishDate.getTime(),
    )
    .slice(0, limit);
}

const SITE = 'https://crismaturana.com';

/**
 * Versiones alternativas en otros idiomas para el <head> (hreflang).
 * Se pasa la ruta EN (p.ej. '/') y la ruta ES (p.ej. '/es/').
 */
export function buildAlternates(enPath: string, esPath: string) {
  return [
    { hreflang: 'en', href: `${SITE}${enPath}` },
    { hreflang: 'es', href: `${SITE}${esPath}` },
    { hreflang: 'x-default', href: `${SITE}${enPath}` },
  ];
}
