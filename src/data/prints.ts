// Catálogo de Prints. Para agregar una foto nueva, copia un bloque y cambia los datos.
// draft: true la oculta del sitio (útil mientras falta la historia).

export type Lang = 'en' | 'es';

export interface PrintSize { id: 's' | 'm' | 'l'; label: string; cm: string; price: number; room: string; }
export interface Print {
  slug: string;
  draft?: boolean;
  image: string;
  title: Record<Lang, string>;
  place: string;
  alt: Record<Lang, string>;
  story: Record<Lang, string[]>;
  meta: Record<Lang, string>;
}

// Precios en USD. room = ancho del print en la foto del living (proporcional al sofá).
export const sizes: PrintSize[] = [
  { id: 's', label: 'S', cm: '30 × 45 cm', price: 95, room: '17%' },
  { id: 'm', label: 'M', cm: '50 × 75 cm', price: 250, room: '26%' },
  { id: 'l', label: 'L', cm: '70 × 105 cm', price: 495, room: '35%' },
];

export const frames = [
  { id: 'black', color: '#1a1714', label: { en: 'Black', es: 'Negro' } },
  { id: 'white', color: '#ddd6c9', label: { en: 'White', es: 'Blanco' } },
  { id: 'oak', color: '#a67c52', label: { en: 'Natural oak', es: 'Roble natural' } },
  { id: 'blue', color: '#2b3b52', label: { en: 'Navy blue', es: 'Azul marino' } },
  { id: 'none', color: 'transparent', label: { en: 'No frame', es: 'Sin marco' } },
];

export const roomImage = '/images/prints/living-gris.webp';

export const prints: Print[] = [
  {
    slug: 'la-risa',
    image: 'https://CrisMaturana.b-cdn.net/Mujer%20Tabaco/DSC_3165-1536x1025.jpg',
    title: { en: 'The Laugh', es: 'La risa' },
    place: 'Hội An, Vietnam',
    alt: {
      en: 'Portrait of an elderly woman in a conical hat, laughing',
      es: 'Retrato de una mujer mayor con sombrero cónico, riendo',
    },
    story: {
      en: [
        'I found her at the market in Hội An, selling vegetables. What caught my eye was that she was chewing trầu, betel leaf with tobacco, a custom kept today mostly by older women. We didn’t share a language, so I asked with gestures if I could photograph her, and she said yes.',
        'We spent ten or fifteen minutes together. She smiled the whole time, happy that someone wanted to take her portrait.',
      ],
      es: [
        'La encontré en el mercado de Hội An, vendiendo vegetales. Me llamó la atención que estaba mascando trầu, hoja de betel con tabaco, una costumbre que hoy conservan sobre todo las mujeres mayores. No hablábamos el mismo idioma, así que le pregunté con señas si podía fotografiarla, y me dijo que sí.',
        'Estuvimos juntos diez o quince minutos. Sonreía todo el tiempo, feliz de que alguien quisiera retratarla.',
      ],
    },
    meta: {
      en: 'Hội An, Vietnam · February 2026 · Nikon D750 · 85 mm',
      es: 'Hội An, Vietnam · Febrero de 2026 · Nikon D750 · 85 mm',
    },
  },
  {
    slug: 'arrozal-al-atardecer',
    image: 'https://CrisMaturana.b-cdn.net/TRAVEL%26CULTURE-SELECTION/01.25HoiAn%40-5.JPG',
    title: { en: 'Rice Field at Sunset', es: 'Arrozal al atardecer' },
    place: 'Hội An, Vietnam',
    alt: {
      en: 'Woman in a conical hat tending a rice field, backlit at sunset',
      es: 'Mujer con sombrero cónico trabajando un arrozal a contraluz, al atardecer',
    },
    story: {
      en: [
        'This rice field is very close to where I live, in Hội An. It is one of the largest in the area. That afternoon, a woman was working among the shoots, already grown a little, separating and arranging them so the rice would grow evenly.',
        'I photographed her from a distance. What held me was the sunset and the backlight falling across the field.',
      ],
      es: [
        'Este arrozal queda muy cerca de donde vivo, en Hội An. Es uno de los más grandes de la zona. Esa tarde, una mujer trabajaba entre los brotes, que ya estaban algo crecidos, separándolos y ordenándolos para que el arroz creciera parejo.',
        'La fotografié de lejos. Me atrapó el atardecer y el contraluz que se formaba sobre el arrozal.',
      ],
    },
    meta: {
      en: 'Hội An, Vietnam · 2025 · Nikon D750 · 85 mm',
      es: 'Hội An, Vietnam · 2025 · Nikon D750 · 85 mm',
    },
  },
  {
    slug: 'el-muelle-de-duy-hai',
    draft: true, // falta la historia
    image: 'https://CrisMaturana.b-cdn.net/TRAVEL%26CULTURE-SELECTION/DuyHaiSeleccion%40-15.JPG',
    title: { en: 'The Duy Hải Pier', es: 'El muelle de Duy Hải' },
    place: 'Duy Hải, Vietnam',
    alt: {
      en: 'Women sitting on a fishing pier with boats behind them, golden light',
      es: 'Mujeres sentadas en un muelle de pescadores con barcos al fondo, luz dorada',
    },
    story: { en: [], es: [] },
    meta: { en: 'Duy Hải, Vietnam', es: 'Duy Hải, Vietnam' },
  },
];

export const publishedPrints = prints.filter((p) => !p.draft);
