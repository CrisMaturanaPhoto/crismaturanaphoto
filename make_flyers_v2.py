import requests, qrcode, io, os, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
import warnings; warnings.filterwarnings("ignore")

SIZE = 500
WEBSITE = "https://crismaturana.com"
FONT = "/System/Library/Fonts/Helvetica.ttc"
OUT = "/Users/matuguz/Documents/GitHub/crismaturanaphoto/flyers"
os.makedirs(OUT, exist_ok=True)

IMGS = {
    "A": "https://CrisMaturana.b-cdn.net/Photo-Tours-Vietnam/DuyHai-SELECTION/DuyHaiSeleccion%40-1.JPG",
    "B": "https://CrisMaturana.b-cdn.net/Photo-Tours-Vietnam/OldTown-SELECTION/01.25HoiAn%40-43.jpg",
    "C": "https://CrisMaturana.b-cdn.net/Photo-Tours-Vietnam/ThuBhonRiver-SELECTION/man-fishing-net-0018.JPEG",
}

def load_img(url, size=SIZE):
    r = requests.get(url, timeout=30)
    img = Image.open(io.BytesIO(r.content)).convert("RGB")
    w, h = img.size; m = min(w, h)
    img = img.crop(((w-m)//2, (h-m)//2, (w-m)//2+m, (h-m)//2+m))
    return img.resize((size, size), Image.LANCZOS)

def f(size):
    try: return ImageFont.truetype(FONT, size)
    except: return ImageFont.load_default()

def qr_img(url, size=160, fill="black", bg="white"):
    q = qrcode.QRCode(version=2, box_size=4, border=2,
                      error_correction=qrcode.constants.ERROR_CORRECT_H)
    q.add_data(url); q.make(fit=True)
    return q.make_image(fill_color=fill, back_color=bg).convert("RGB").resize((size,size), Image.LANCZOS)

def ctext(draw, text, y, fnt, color, w=SIZE):
    bb = draw.textbbox((0,0), text, font=fnt)
    draw.text(((w-(bb[2]-bb[0]))//2, y), text, font=fnt, fill=color)

def noise_layer(size, opacity=30):
    """Grain texture overlay"""
    random.seed(42)
    noise = Image.new("L", (size, size))
    pix = noise.load()
    for x in range(size):
        for y in range(size):
            pix[x,y] = random.randint(0, 255)
    noise = noise.filter(ImageFilter.GaussianBlur(0.3))
    layer = Image.new("RGBA", (size, size), (0,0,0,0))
    layer.putalpha(noise.point(lambda p: int(p * opacity / 255)))
    return layer

# ══════════════════════════════════════════════════════════
# DISEÑO 4 — NEO-BRUTALISM
# Tendencia: bordes gruesos negros, amarillo eléctrico,
# offset shadows, tipografía raw, composición asimétrica
# Imagen: Barcos DuyHai
# ══════════════════════════════════════════════════════════
ELEC  = (255, 229, 0)    # amarillo eléctrico
BLK   = (10, 10, 10)
WHT   = (255, 255, 255)
BRUT_RED = (255, 40, 30)

def d4_front():
    base = Image.new("RGB", (SIZE, SIZE), ELEC)
    draw = ImageDraw.Draw(base)

    # Foto con offset shadow brutalista
    photo = load_img(IMGS["A"]).resize((330, 330), Image.LANCZOS)
    # sombra offset sólida negra
    shadow = Image.new("RGB", (330, 330), BLK)
    base.paste(shadow, (32+8, 38+8))          # offset shadow
    base.paste(photo, (32, 38))
    # borde grueso negro alrededor de la foto
    draw.rectangle([(32,38),(32+330,38+330)], outline=BLK, width=4)

    # Texto brutalist — grande y crudo
    draw.text((32, 378), "PHOTO", font=f(72), fill=BLK)
    draw.text((32, 440), "TOURS", font=f(72), fill=BRUT_RED)

    # Panel lateral derecho — franja negra vertical
    draw.rectangle([(375, 38), (490, 368)], fill=BLK)
    # texto rotado vertical (simulado con letras)
    for i, ch in enumerate("HOI AN · VIETNAM"):
        draw.text((385, 45 + i*18), ch, font=f(12), fill=ELEC)

    # Año en esquina
    draw.rectangle([(375, 375),(490, 408)], fill=BLK)
    draw.text((385, 382), "2025–26", font=f(13), fill=ELEC)

    # Líneas decorativas brutalistas
    draw.rectangle([(0, 0),(SIZE,10)], fill=BLK)
    draw.rectangle([(0, SIZE-10),(SIZE,SIZE)], fill=BLK)
    draw.rectangle([(0,0),(10,SIZE)], fill=BLK)

    # crismaturana.com
    draw.rectangle([(0, SIZE-10),(SIZE,SIZE)], fill=BLK)
    ctext(draw, "crismaturana.com", SIZE-38, f(14), ELEC)

    return base

def d4_back():
    base = Image.new("RGB", (SIZE, SIZE), ELEC)
    draw = ImageDraw.Draw(base)

    # Marco brutalista con offset
    shadow_frame = Image.new("RGB", (460, 460), BLK)
    base.paste(shadow_frame, (28, 28))
    inner = Image.new("RGB", (452, 452), WHT)
    base.paste(inner, (24, 24))
    draw.rectangle([(24,24),(476,476)], outline=BLK, width=4)

    draw.rectangle([(24,24),(476,80)], fill=BLK)
    ctext(draw, "SCAN & BOOK", 33, f(28), ELEC)
    ctext(draw, "YOUR TOUR", 59, f(14), ELEC)

    # QR grande
    q = qr_img(WEBSITE, 200, fill="black", bg="white")
    base.paste(q, ((SIZE-200)//2, 95))

    draw.rectangle([(24,308),(476,312)], fill=BLK)

    ctext(draw, "crismaturana.com", 320, f(20), BLK)
    ctext(draw, "HOI AN  ·  VIETNAM  ·  2026", 352, f(12), BLK)

    draw.rectangle([(24,380),(476,381)], fill=BLK)

    infos = ["Small groups · Max 6", "Golden hour sessions", "All skill levels welcome", "@crismaturanaphoto"]
    for i, t in enumerate(infos):
        ctext(draw, t, 392 + i*18, f(12), BLK)

    draw.rectangle([(24,460),(476,476)], fill=BLK)
    ctext(draw, "PHOTO TOURS HOI AN · VIETNAM", 463, f(9), ELEC)

    return base


# ══════════════════════════════════════════════════════════
# DISEÑO 5 — AURORA GRADIENT / GLASSMORPHISM
# Tendencia: mesh gradient oscuro (morado→teal→ámbar),
# frosted glass panel, foto con duotono, partículas flotantes
# Imagen: Old Town / barca
# ══════════════════════════════════════════════════════════
def aurora_bg():
    """Fondo tipo aurora borealis / mesh gradient"""
    bg = Image.new("RGB", (SIZE, SIZE), (8, 4, 22))
    draw = ImageDraw.Draw(bg)

    # Blobs de color difusos
    blobs = [
        ((80,  60),  180, (120, 40, 160)),   # morado
        ((380, 80),  160, (20, 140, 160)),   # teal
        ((60,  380), 140, (180, 80, 20)),    # ámbar
        ((400, 380), 160, (40, 60, 180)),    # azul
        ((230, 220), 120, (80, 160, 100)),   # verde medio
    ]
    for (cx, cy), r, color in blobs:
        for radius in range(r, 0, -2):
            alpha = int(120 * (1 - radius/r))
            r_val = int(color[0] * (1 - radius/r * 0.3))
            g_val = int(color[1] * (1 - radius/r * 0.3))
            b_val = int(color[2] * (1 - radius/r * 0.3))
            draw.ellipse([(cx-radius, cy-radius),(cx+radius, cy+radius)],
                         fill=(r_val, g_val, b_val))

    bg = bg.filter(ImageFilter.GaussianBlur(45))
    return bg

def frosted_panel(size_w, size_h, tint=(255,255,255), alpha=35):
    """Panel tipo glass morphism"""
    panel = Image.new("RGBA", (size_w, size_h), (*tint, alpha))
    return panel

def d5_front():
    bg = aurora_bg()

    # Foto con duotono (tono morado→teal)
    photo = load_img(IMGS["B"]).resize((320, 320), Image.LANCZOS)
    gray = photo.convert("L")
    # mapear gris a duotono morado→ámbar
    duotone = Image.new("RGB", (320, 320))
    pix_src = gray.load()
    pix_dst = duotone.load()
    for x in range(320):
        for y in range(320):
            t = pix_src[x,y] / 255
            r = int(20 + t * 235)
            g = int(10 + t * 180)
            b = int(80 + t * 100)
            pix_dst[x,y] = (r, g, b)
    # blend 50% foto real + 50% duotono
    blended = Image.blend(photo, duotone, 0.45)

    # Máscara circular
    mask_c = Image.new("L", (320, 320), 0)
    ImageDraw.Draw(mask_c).ellipse([(0,0),(319,319)], fill=255)
    # borde exterior glow
    glow = Image.new("RGB", (340, 340), (80, 40, 120))
    glow_mask = Image.new("L", (340, 340), 0)
    ImageDraw.Draw(glow_mask).ellipse([(0,0),(339,339)], fill=200)
    glow_mask = glow_mask.filter(ImageFilter.GaussianBlur(8))

    base = bg.convert("RGBA")
    glow_layer = Image.new("RGBA", (SIZE, SIZE), (0,0,0,0))
    glow_layer.paste(Image.new("RGBA",(340,340),(100,50,180,120)), (80, 70), glow_mask)
    base = Image.alpha_composite(base, glow_layer)

    base_rgb = base.convert("RGB")
    base_rgb.paste(blended, (90, 80), mask_c)

    # Anillo decorativo
    ring_layer = Image.new("RGBA", (SIZE, SIZE), (0,0,0,0))
    ring_draw = ImageDraw.Draw(ring_layer)
    ring_draw.ellipse([(86,76),(414,404)], outline=(200,150,255,120), width=2)
    ring_draw.ellipse([(80,70),(420,410)], outline=(100,200,200,60), width=1)
    base_rgb = Image.alpha_composite(base_rgb.convert("RGBA"), ring_layer).convert("RGB")

    # Panel glass inferior
    glass = frosted_panel(SIZE-60, 135, tint=(200,180,255), alpha=30)
    glass_img = Image.new("RGBA", (SIZE, SIZE), (0,0,0,0))
    glass_img.paste(glass, (30, 345))
    base_rgb = Image.alpha_composite(base_rgb.convert("RGBA"), glass_img).convert("RGB")

    # Borde panel glass
    d = ImageDraw.Draw(base_rgb)
    d.rectangle([(30,345),(SIZE-30,480)], outline=(200,150,255,160), width=1)

    # Grano de película
    grain = noise_layer(SIZE, 18)
    base_rgba = base_rgb.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, grain)
    base_rgb = base_rgba.convert("RGB")

    draw = ImageDraw.Draw(base_rgb)

    # Pequeño tag
    draw.rounded_rectangle([(90,355),(260,375)], radius=10, fill=(255,200,100,0))
    ctext(draw, "✦  PHOTO EXPERIENCE  ✦", 355, f(11), (255, 210, 120))

    ctext(draw, "PHOTO TOURS", 376, f(38), (255, 255, 255))
    ctext(draw, "HOI AN · VIETNAM", 420, f(18), (180, 220, 255))
    ctext(draw, "crismaturana.com", 450, f(12), (150, 180, 220))

    # Puntos decorativos top
    for i in range(5):
        draw.ellipse([(60+i*90, 52),(65+i*90, 57)], fill=(200,150,255,200))

    return base_rgb

def d5_back():
    bg = aurora_bg()
    base = bg.convert("RGBA")

    # Panel glass central grande
    glass = frosted_panel(360, 360, tint=(200, 220, 255), alpha=25)
    glass_img = Image.new("RGBA", (SIZE, SIZE), (0,0,0,0))
    glass_img.paste(glass, (70, 70))
    base = Image.alpha_composite(base, glass_img)

    # Borde del panel glass
    d_layer = Image.new("RGBA", (SIZE, SIZE), (0,0,0,0))
    d_draw = ImageDraw.Draw(d_layer)
    d_draw.rounded_rectangle([(70,70),(430,430)], radius=16,
                               outline=(180, 150, 255, 140), width=2)
    base = Image.alpha_composite(base, d_layer)
    base_rgb = base.convert("RGB")
    draw = ImageDraw.Draw(base_rgb)

    ctext(draw, "SCAN TO EXPLORE", 88, f(14), (220, 200, 255))
    draw.rectangle([(120, 110),(SIZE-120, 111)], fill=(180,150,255,150))

    q = qr_img(WEBSITE, 175, fill=(20,8,50), bg=(240,235,255))
    base_rgb.paste(q, ((SIZE-175)//2, 118))

    draw.rectangle([(120,304),(SIZE-120,305)], fill=(180,150,255,100))

    ctext(draw, "crismaturana.com", 316, f(18), (255,255,255))
    ctext(draw, "HOI AN  ·  VIETNAM", 344, f(12), (180, 220, 255))

    draw.rectangle([(120,372),(SIZE-120,373)], fill=(180,150,255,80))

    features = ["🌅  Dawn & dusk sessions", "👥  Small group · Max 6", "📷  All skill levels"]
    for i, t in enumerate(features):
        ctext(draw, t, 384+i*22, f(12), (200, 210, 230))

    ctext(draw, "@crismaturanaphoto", 460, f(13), (200, 160, 255))

    grain = noise_layer(SIZE, 15)
    base_rgba = base_rgb.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, grain)
    return base_rgba.convert("RGB")


# ══════════════════════════════════════════════════════════
# DISEÑO 6 — EDITORIAL MAGAZINE / TYPOGRAPHIC
# Tendencia: tipografía gigante que sangra, foto como textura,
# composición asimétrica extrema, color block, línea editorial
# Imagen: Pescador en red
# ══════════════════════════════════════════════════════════
CREAM  = (245, 240, 225)
INK    = (18, 15, 12)
RUST   = (185, 65, 35)
WARM   = (210, 195, 170)

def d6_front():
    base = Image.new("RGB", (SIZE, SIZE), CREAM)

    # Foto ocupa zona superior — con viñeta
    photo = load_img(IMGS["C"]).resize((SIZE, 310), Image.LANCZOS)
    en = ImageEnhance.Contrast(photo)
    photo = en.enhance(1.15)
    en2 = ImageEnhance.Color(photo)
    photo = en2.enhance(0.75)  # ligeramente desaturada

    # Viñeta en foto
    vig = Image.new("RGBA", (SIZE, 310), (0,0,0,0))
    vd = ImageDraw.Draw(vig)
    for i in range(80):
        alpha = int(180 * (i/80))
        vd.rectangle([(0, 310-80+i),(SIZE, 310-80+i+1)], fill=(245,240,225,alpha))

    base.paste(photo, (0, 0))
    base_rgba = base.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, Image.new("RGBA",(SIZE,SIZE),(0,0,0,0)))
    vig_full = Image.new("RGBA", (SIZE, SIZE), (0,0,0,0))
    vig_full.paste(vig, (0, 0))
    base_rgba = Image.alpha_composite(base_rgba, vig_full)
    base = base_rgba.convert("RGB")

    draw = ImageDraw.Draw(base)

    # Línea editorial roja horizontal
    draw.rectangle([(0, 308),(SIZE, 314)], fill=RUST)
    draw.rectangle([(0, 318),(SIZE, 320)], fill=RUST)

    # Tipografía editorial gigante — "PHOTO" sangra a la izquierda
    draw.text((-4, 310), "PHOTO", font=f(88), fill=INK)

    # "TOURS" en rust
    draw.text((6, 388), "TOURS", font=f(64), fill=RUST)

    # Texto derecho pequeño, columna editorial
    small_lines = ["HOI AN", "VIETNAM", "2026"]
    for i, line in enumerate(small_lines):
        draw.text((390, 318+i*26), line, font=f(15), fill=INK)

    # Punto rojo decorativo
    draw.ellipse([(385, 396),(398, 409)], fill=RUST)

    # Filete inferior
    draw.rectangle([(0, SIZE-42),(SIZE, SIZE)], fill=INK)
    ctext(draw, "crismaturana.com  ·  PHOTO TOURS", SIZE-28, f(13), CREAM)

    # Número de edición editorial
    draw.text((10, SIZE-44), "VOL. 01", font=f(9), fill=WARM)

    # Grano de película
    grain = noise_layer(SIZE, 25)
    base_rgba = base.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, grain)
    return base_rgba.convert("RGB")

def d6_back():
    base = Image.new("RGB", (SIZE, SIZE), CREAM)
    draw = ImageDraw.Draw(base)

    # Bloque negro superior tipográfico
    draw.rectangle([(0,0),(SIZE, 90)], fill=INK)
    ctext(draw, "PHOTO TOURS", 12, f(36), CREAM)
    ctext(draw, "HOI AN · VIETNAM", 56, f(16), RUST)

    # Líneas editoriales
    draw.rectangle([(40, 96),(SIZE-40, 98)], fill=RUST)
    draw.rectangle([(40,102),(SIZE-40,103)], fill=INK)

    # QR con marco tipo editorial
    q = qr_img(WEBSITE, 185, fill=INK, bg=CREAM)
    # marco rojo
    frame = Image.new("RGB", (191, 191), RUST)
    frame.paste(q, (3, 3))
    base.paste(frame, ((SIZE-191)//2, 110))

    draw.rectangle([(40, 310),(SIZE-40, 312)], fill=INK)
    draw.rectangle([(40, 316),(SIZE-40, 317)], fill=RUST)

    ctext(draw, "Scan to book", 326, f(14), INK)
    ctext(draw, "crismaturana.com", 348, f(22), INK)

    draw.rectangle([(40, 382),(SIZE-40, 383)], fill=WARM)

    cols = [
        ("LOCATION", "Hoi An, Vietnam"),
        ("GROUPS",   "Max 6 people"),
        ("LIGHT",    "Dawn & dusk"),
        ("CONTACT",  "@crismaturanaphoto"),
    ]
    col_x = [40, 260]
    for i, (label, val) in enumerate(cols):
        x = col_x[i % 2]
        y = 394 + (i//2)*44
        draw.text((x, y), label, font=f(9), fill=RUST)
        draw.text((x, y+13), val, font=f(12), fill=INK)

    draw.rectangle([(0,SIZE-38),(SIZE,SIZE)], fill=INK)
    ctext(draw, "PHOTO TOURS HOI AN · VOL. 01 · 2026", SIZE-24, f(9), CREAM)

    grain = noise_layer(SIZE, 20)
    base_rgba = base.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, grain)
    return base_rgba.convert("RGB")


# ──────────────────────────────────────────────
print("Generando Diseño 4 — Neo-Brutalism...")
d4_front().save(f"{OUT}/flyer4_front.jpg", quality=95)
d4_back().save(f"{OUT}/flyer4_back.jpg", quality=95)
print("Generando Diseño 5 — Aurora/Glassmorphism...")
d5_front().save(f"{OUT}/flyer5_front.jpg", quality=95)
d5_back().save(f"{OUT}/flyer5_back.jpg", quality=95)
print("Generando Diseño 6 — Editorial Magazine...")
d6_front().save(f"{OUT}/flyer6_front.jpg", quality=95)
d6_back().save(f"{OUT}/flyer6_back.jpg", quality=95)
print("✓ Done — 6 archivos en /flyers/")
