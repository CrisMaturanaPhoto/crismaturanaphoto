// ui.ts — Datos de presentación de la home (compartidos EN/ES).
// Los textos visibles aquí son fallback en inglés; la traducción real
// la aplica translations.js vía data-i18n. Las URLs e imágenes son neutras.

export interface HeroSlide {
  title: string;
  subtitle: string;
  cta: string;
  href: string;
  bg: string;
  focus?: string;
}

export interface PortfolioCategory {
  title: string;
  subtitle?: string;
  href: string;
  thumb: string;
  focus?: string;
}

export const heroSlides: HeroSlide[] = [
  {
    title: 'Documentary Weddings',
    subtitle: 'DESTINATION DOCUMENTARY PHOTOGRAPHER',
    cta: 'View Portfolio',
    href: '/hoi-an-wedding-photographer',
    bg: 'https://CrisMaturana.b-cdn.net/WEDDINGS-SELECTION/Poppin%26Chris-Wedding-%40-228.jpg',
  },
  {
    title: 'Couples & Families',
    subtitle: 'REAL MOMENTS. HONEST CONNECTION.',
    cta: 'Find More',
    href: '/family-portrait-photography-hoi-an',
    bg: 'https://CrisMaturana.b-cdn.net/COUPLES%26FAMILY-SELECTION/Gina%26Nick%40-113.JPG',
  },
  {
    title: 'Documentary Weddings',
    subtitle: 'DESTINATION DOCUMENTARY PHOTOGRAPHER',
    cta: 'Find More',
    href: '/hoi-an-wedding-photographer',
    bg: 'https://CrisMaturana.b-cdn.net/WEDDINGS-SELECTION/poppin-chris-005.JPG',
  },
  {
    title: 'Photo Tours Vietnam',
    subtitle: 'DESTINATION DOCUMENTARY PHOTOGRAPHER',
    cta: 'Find More',
    href: '/photo-tours-vietnam-2026',
    bg: 'https://CrisMaturana.b-cdn.net/TRAVEL%26CULTURE-SELECTION/DuyHaiSeleccion%40-10.JPG',
  },
];

// Las primeras 4 son los servicios principales (grid grande).
// Las ultimas 2 son categorias secundarias de portfolio (fila chica abajo).
export const portfolioCategories: PortfolioCategory[] = [
  {
    title: 'Weddings & Elopements',
    subtitle: 'Moments that last forever.',
    href: '/hoi-an-wedding-photographer',
    thumb: 'https://CrisMaturana.b-cdn.net/WEDDINGS-SELECTION/Yaz-Li-portrait-001.jpg',
  },
  {
    title: 'Portraits & Families',
    subtitle: 'Genuine connection, beautifully captured.',
    href: '/family-portrait-photography-hoi-an',
    thumb: 'https://CrisMaturana.b-cdn.net/COUPLES%26FAMILY-SELECTION/Alistair%26Emma-10.jpg',
  },
  {
    title: 'Brand & Lifestyle',
    subtitle: 'Natural light. Honest expressions.',
    href: '/personal-branding-photography-hoi-an',
    thumb: 'https://CrisMaturana.b-cdn.net/PORTRAITS-SELECTION/MartinsSoul%40-26.JPG',
    focus: 'center top',
  },
  {
    title: 'Photography Tours',
    subtitle: 'Photograph Vietnam the way it really is.',
    href: '/photo-tours-vietnam-2026',
    thumb: 'https://CrisMaturana.b-cdn.net/Photo-Tours-Vietnam/OldTown-SELECTION/01.25HoiAn%40-43.jpg',
  },
  {
    title: 'Travel & Culture',
    subtitle: 'Observing the world, honestly.',
    href: '/portfolio/travel-culture',
    thumb: 'https://CrisMaturana.b-cdn.net/TRAVEL%26CULTURE-SELECTION/01.25HoiAn%40-5.JPG',
  },
  {
    title: 'From Above',
    subtitle: 'Perspective changes everything.',
    href: '/portfolio/aerial',
    thumb: 'https://CrisMaturana.b-cdn.net/FROMABOVE-SELECTION/atacama-desert-001.JPG',
  },
];
