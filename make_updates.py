"""
Actualiza:
  - flyer1_front/back: título arriba en el cielo, logos IG/FB en reverso
  - flyer6_front/back: foto DuyHai sin deformar, reverso fondo blanco rediseñado
"""
import requests, qrcode, io, os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import warnings; warnings.filterwarnings("ignore")

SIZE    = 500
WEBSITE = "https://crismaturana.com"
FONT    = "/System/Library/Fonts/Helvetica.ttc"
OUT     = "/Users/matuguz/Documents/GitHub/crismaturanaphoto/flyers"

IMGS = {
    "A": "https://CrisMaturana.b-cdn.net/Photo-Tours-Vietnam/DuyHai-SELECTION/DuyHaiSeleccion%40-1.JPG",
}

GOLD  = (212, 175, 55)
WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
RED   = (185, 55, 35)
CREAM = (245, 240, 225)
INK   = (18, 15, 12)
RUST  = (185, 65, 35)
WARM  = (210, 195, 170)

def load_full(url):
    """Carga imagen SIN recortar — mantiene proporciones originales."""
    r = requests.get(url, timeout=30)
    return Image.open(io.BytesIO(r.content)).convert("RGB")

def load_square(url):
    """Recorta al centro para hacer cuadrado 500x500."""
    img = load_full(url)
    w, h = img.size
    m = min(w, h)
    img = img.crop(((w-m)//2, (h-m)//2, (w+m)//2, (h+m)//2))
    return img.resize((SIZE, SIZE), Image.LANCZOS)

def f(size):
    try: return ImageFont.truetype(FONT, size)
    except: return ImageFont.load_default()

def ctext(draw, text, y, fnt, color, w=SIZE):
    bb = draw.textbbox((0,0), text, font=fnt)
    draw.text(((w-(bb[2]-bb[0]))//2, y), text, font=fnt, fill=color)

def shadow_text(draw, text, y, fnt, color, shadow=(0,0,0,160), w=SIZE):
    bb = draw.textbbox((0,0), text, font=fnt)
    x = (w-(bb[2]-bb[0]))//2
    draw.text((x+2, y+2), text, font=fnt, fill=shadow)
    draw.text((x, y), text, font=fnt, fill=color)

def make_qr(url, size=180):
    q = qrcode.QRCode(version=2, box_size=4, border=2,
                      error_correction=qrcode.constants.ERROR_CORRECT_H)
    q.add_data(url); q.make(fit=True)
    return q.make_image(fill_color="black", back_color="white").convert("RGB").resize((size,size), Image.LANCZOS)

def ig_icon(size=28, color=(160,160,220)):
    """Icono Instagram sobrio — solo contorno, sin relleno de color."""
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    d = ImageDraw.Draw(img)
    m = 1
    # contorno redondeado sin fondo
    d.rounded_rectangle([(m,m),(size-m-1,size-m-1)], radius=size//4,
                         outline=color, width=2)
    # círculo central
    r = size//2
    cr = size//5
    d.ellipse([(r-cr, r-cr),(r+cr, r+cr)], outline=color, width=2)
    # punto esquina superior derecha
    dp = size//5
    d.ellipse([(size-dp-3, dp-1),(size-dp+1, dp+3)], fill=color)
    return img

def fb_icon(size=28):
    """Icono Facebook dibujado con Pillow."""
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([(0,0),(size-1,size-1)], radius=size//4,
                         fill=(24, 119, 242))
    # "f" simplificada
    fw = size//5
    fh = size//2
    fx = size//2 - fw//2 + 2
    fy = size//4
    d.rectangle([(fx, fy),(fx+fw, fy+fh+fw)], fill=(255,255,255,255))
    # barra horizontal
    d.rectangle([(fx-fw//2, fy+fh//3),(fx+fw+fw//2, fy+fh//3+fw//2)],
                fill=(24,119,242))
    # arco superior (cabeza de f)
    d.arc([(fx-fw//2, fy-fw),(fx+fw+fw, fy+fw)], start=200, end=340,
          fill=(255,255,255,255), width=2)
    return img

# ══════════════════════════════════════════════════════════
# DISEÑO 1 ACTUALIZADO
# Frente: título en el cielo (arriba), no tapa barcos/banderas
# Reverso: logos IG + FB junto a @crismaturanaphoto
# ══════════════════════════════════════════════════════════
def d1_front_v2():
    P = 1417  # 12x12cm a 300dpi

    # Cargar y escalar foto a P×P
    raw = load_full(IMGS["A"])
    rw, rh = raw.size
    m = min(rw, rh)
    raw = raw.crop(((rw-m)//2, (rh-m)//2, (rw+m)//2, (rh+m)//2))
    img = raw.resize((P, P), Image.LANCZOS)

    overlay = Image.new("RGBA", (P, P), (0,0,0,0))
    d = ImageDraw.Draw(overlay)

    # Gradiente oscuro superior para leer el título
    for i in range(560):
        alpha = int(210 * (1 - i/560))
        d.rectangle([(0, i),(P, i+1)], fill=(0,0,0,alpha))

    base = img.convert("RGBA")
    base = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(base)

    # TÍTULO en la zona del cielo
    shadow_text(draw, "PHOTO TOURS", 100, f(174), (*WHITE, 255), w=P)
    shadow_text(draw, "HOI AN · VIETNAM", 296, f(78), (*GOLD, 255), w=P)

    return base.convert("RGB")

def d1_back_v2():
    P = 1417  # 12x12cm a 300dpi
    bg = Image.new("RGB", (P, P), (10, 10, 20))
    bg.info['dpi'] = (300, 300)
    draw = ImageDraw.Draw(bg)

    # Marco dorado
    draw.rectangle([(0,0),(P,11)], fill=GOLD)
    draw.rectangle([(0,P-11),(P,P)], fill=GOLD)
    draw.rectangle([(0,0),(11,P)], fill=GOLD)
    draw.rectangle([(P-11,0),(P,P)], fill=GOLD)

    ctext(draw, "PHOTO TOURS HOI AN", 60, f(80), GOLD, P)
    ctext(draw, "VIETNAM", 158, f(80), (180,180,180), P)

    # QR grande
    qr = make_qr(WEBSITE, 480)
    bg.paste(qr, ((P-480)//2, 268))

    # Separador
    draw.rectangle([(150, 768),(P-150, 771)], fill=(60,60,60))

    ctext(draw, "Scan to explore & book", 790, f(60), (200,200,200), P)
    ctext(draw, "crismaturana.com", 864, f(60), GOLD, P)

    draw.rectangle([(150, 948),(P-150, 951)], fill=(60,60,60))

    ctext(draw, "Small group photo tours  ·  Dawn & dusk light", 970, f(60), (120,120,120), P)
    ctext(draw, "Hoi An, Vietnam  ·  Est. 2022", 1044, f(60), (100,100,100), P)

    draw.rectangle([(150, 1200),(P-150, 1203)], fill=(60,60,60))

    # IG + handle
    ig = ig_icon(72, color=(160,160,220))
    handle = "@crismaturanaphoto"
    bb = draw.textbbox((0,0), handle, font=f(60))
    tw = bb[2]-bb[0]
    total_w = 72 + 18 + tw
    sx = (P - total_w) // 2
    bg.paste(ig, (sx, 1218), ig)
    draw.text((sx + 90, 1228), handle, font=f(60), fill=(160,160,220))

    return bg


# ══════════════════════════════════════════════════════════
# DISEÑO 6 ACTUALIZADO
# Frente: foto DuyHai sin deformar, estilo editorial
# Reverso: fondo BLANCO, "PHOTO" negro, "TOURS" rojo,
#          "HOI AN VIETNAM" negro
# ══════════════════════════════════════════════════════════
def d6_front_v2():
    RED_LINE = 320  # posición de la línea roja
    base = Image.new("RGB", (SIZE, SIZE), CREAM)

    # Escalar por ANCHO = 500px para no deformar (foto landscape)
    raw = load_full(IMGS["A"])
    rw, rh = raw.size
    scale = SIZE / rw
    new_h = int(rh * scale)
    raw = raw.resize((SIZE, new_h), Image.LANCZOS)
    # Tomar desde el TOP — así vemos cielo + barcos + banderas
    photo_strip = raw.crop((0, 0, SIZE, RED_LINE))

    # Leve desaturación para aspecto editorial
    base.paste(photo_strip, (0, 0))

    draw = ImageDraw.Draw(base)

    # Filetes editoriales sobre la línea roja
    draw.rectangle([(0, RED_LINE),(SIZE, RED_LINE+5)], fill=RUST)
    draw.rectangle([(0, RED_LINE+9),(SIZE, RED_LINE+11)], fill=INK)

    # "PHOTO" grande que empieza justo bajo la línea roja
    draw.text((-3, RED_LINE+2), "PHOTO", font=f(86), fill=INK)

    # "TOURS" en rust
    draw.text((8, RED_LINE+80), "TOURS", font=f(62), fill=RUST)

    # Columna editorial derecha
    for i, line in enumerate(["HOI AN", "VIETNAM", "2026"]):
        draw.text((392, RED_LINE+12+i*26), line, font=f(14), fill=INK)

    # Punto rojo
    draw.ellipse([(388, RED_LINE+88),(401, RED_LINE+101)], fill=RUST)

    # Barra inferior
    draw.rectangle([(0, SIZE-40),(SIZE, SIZE)], fill=INK)
    ctext(draw, "crismaturana.com  ·  PHOTO TOURS", SIZE-26, f(13), CREAM)
    draw.text((10, SIZE-42), "VOL. 01", font=f(9), fill=WARM)

    return base

def d6_back_v2():
    """Reverso: fondo BLANCO, tipografía negra/roja, QR, info."""
    base = Image.new("RGB", (SIZE, SIZE), WHITE)
    draw = ImageDraw.Draw(base)

    # Título tipográfico grande — fondo blanco
    # "PHOTO" negro
    shadow_text(draw, "PHOTO", 22, f(72), BLACK, shadow=(0,0,0,30))
    # "TOURS" rojo
    shadow_text(draw, "TOURS", 96, f(72), RED, shadow=(0,0,0,20))
    # "HOI AN  VIETNAM" negro, más pequeño
    shadow_text(draw, "HOI AN  ·  VIETNAM", 170, f(24), BLACK, shadow=(0,0,0,20))

    # Filete rojo
    draw.rectangle([(40, 202),(SIZE-40, 205)], fill=RED)
    draw.rectangle([(40, 209),(SIZE-40, 210)], fill=BLACK)

    # QR centrado
    qr = make_qr(WEBSITE, 170)
    # marco negro fino
    frame = Image.new("RGB", (176, 176), BLACK)
    frame.paste(qr, (3, 3))
    base.paste(frame, ((SIZE-176)//2, 216))

    draw.rectangle([(40, 400),(SIZE-40, 402)], fill=BLACK)
    draw.rectangle([(40, 406),(SIZE-40, 407)], fill=RED)

    ctext(draw, "Scan to book your tour", 415, f(13), (60,60,60))
    ctext(draw, "crismaturana.com", 438, f(19), BLACK)
    ctext(draw, "@crismaturanaphoto", 468, f(13), (80,80,80))

    # Filetes laterales decorativos (sutil)
    draw.rectangle([(0,0),(4,SIZE)], fill=RED)
    draw.rectangle([(SIZE-4,0),(SIZE,SIZE)], fill=RED)
    draw.rectangle([(0,0),(SIZE,4)], fill=BLACK)
    draw.rectangle([(0,SIZE-4),(SIZE,SIZE)], fill=BLACK)

    return base


# ─── Generar ───────────────────────────────────────────
print("Actualizando Diseño 1...")
d1_front_v2().save(f"{OUT}/flyer1_front.jpg", quality=95)
d1_back_v2().save(f"{OUT}/flyer1_back.jpg", quality=95)

print("Actualizando Diseño 6...")
d6_front_v2().save(f"{OUT}/flyer6_front.jpg", quality=95)
d6_back_v2().save(f"{OUT}/flyer6_back.jpg", quality=95)

print("✓ Listo")
