import requests
import qrcode
import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import warnings
warnings.filterwarnings("ignore")

SIZE = 500
WEBSITE = "https://crismaturana.com"
FONT_PATH = "/System/Library/Fonts/Helvetica.ttc"

IMGS = {
    "A": "https://CrisMaturana.b-cdn.net/Photo-Tours-Vietnam/DuyHai-SELECTION/DuyHaiSeleccion%40-1.JPG",
    "B": "https://CrisMaturana.b-cdn.net/Photo-Tours-Vietnam/OldTown-SELECTION/01.25HoiAn%40-43.jpg",
    "C": "https://CrisMaturana.b-cdn.net/Photo-Tours-Vietnam/ThuBhonRiver-SELECTION/man-fishing-net-0018.JPEG",
}

def load_image(url):
    r = requests.get(url, timeout=30)
    img = Image.open(io.BytesIO(r.content)).convert("RGB")
    # crop to square from center
    w, h = img.size
    m = min(w, h)
    left = (w - m) // 2
    top = (h - m) // 2
    img = img.crop((left, top, left + m, top + m))
    return img.resize((SIZE, SIZE), Image.LANCZOS)

def make_qr(url, size=180):
    qr = qrcode.QRCode(version=2, box_size=4, border=2,
                       error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return qr_img.resize((size, size), Image.LANCZOS)

def font(size, bold=False):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except:
        return ImageFont.load_default()

def center_text(draw, text, y, w, fnt, color):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, y), text, font=fnt, fill=color)

def draw_text_with_shadow(draw, text, y, w, fnt, color, shadow_color=(0,0,0,120)):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    x = (w - tw) // 2
    draw.text((x+2, y+2), text, font=fnt, fill=shadow_color)
    draw.text((x, y), text, font=fnt, fill=color)

# ──────────────────────────────────────────────
# DISEÑO 1 — Foto full bleed · título grande · overlay oscuro inferior
# Imagen: DuyHai (barcos con banderas vietnamitas)
# Paleta: imagen real + texto blanco
# ──────────────────────────────────────────────
def design1_front():
    img = load_image(IMGS["A"])
    overlay = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    # gradiente oscuro abajo
    for i in range(220):
        alpha = int(210 * (i / 220))
        d.rectangle([(0, SIZE - 220 + i), (SIZE, SIZE - 220 + i + 1)], fill=(0, 0, 0, alpha))
    # franja oscura arriba fina
    d.rectangle([(0, 0), (SIZE, 50)], fill=(0, 0, 0, 140))

    base = img.convert("RGBA")
    base = Image.alpha_composite(base, overlay)
    draw = ImageDraw.Draw(base)

    # línea dorada decorativa
    draw.rectangle([(30, 45), (SIZE - 30, 47)], fill=(212, 175, 55, 255))

    # TAG superior
    draw.text((36, 16), "✦  EXPERIENCE VIETNAM  ✦", font=font(11), fill=(212, 175, 55, 255))

    # Título grande
    draw_text_with_shadow(draw, "PHOTO TOURS", SIZE - 200, SIZE, font(62), (255, 255, 255, 255))
    draw_text_with_shadow(draw, "HOI AN · VIETNAM", SIZE - 135, SIZE, font(28), (212, 175, 55, 255))

    # Subtítulo
    center_text(draw, "Small groups  ·  Authentic light  ·  Real stories", SIZE - 68, SIZE, font(13), (220, 220, 220, 220))
    center_text(draw, "crismaturana.com", SIZE - 44, SIZE, font(12), (180, 180, 180, 200))

    return base.convert("RGB")

def design1_back():
    bg = Image.new("RGB", (SIZE, SIZE), (10, 10, 20))
    draw = ImageDraw.Draw(bg)

    # líneas decorativas
    draw.rectangle([(0, 0), (SIZE, 4)], fill=(212, 175, 55))
    draw.rectangle([(0, SIZE - 4), (SIZE, SIZE)], fill=(212, 175, 55))
    draw.rectangle([(0, 0), (4, SIZE)], fill=(212, 175, 55))
    draw.rectangle([(SIZE - 4, 0), (SIZE, SIZE)], fill=(212, 175, 55))

    center_text(draw, "PHOTO TOURS HOI AN", 28, SIZE, font(22), (212, 175, 55))
    center_text(draw, "VIETNAM", 58, SIZE, font(14), (180, 180, 180))

    # QR
    qr = make_qr(WEBSITE, 180)
    bg.paste(qr, ((SIZE - 180) // 2, 95))

    center_text(draw, "Scan to explore & book", 290, SIZE, font(14), (200, 200, 200))
    center_text(draw, "crismaturana.com", 315, SIZE, font(16), (212, 175, 55))

    draw.rectangle([(60, 360), (SIZE - 60, 361)], fill=(60, 60, 60))

    center_text(draw, "📸  Cris Maturana Photography", 372, SIZE, font(13), (160, 160, 160))
    center_text(draw, "Small group photo tours · Dawn & dusk light", 396, SIZE, font(12), (120, 120, 120))
    center_text(draw, "Hoi An, Vietnam  ·  Est. 2022", 418, SIZE, font(11), (100, 100, 100))

    # Instagram
    center_text(draw, "@crismaturanaphoto", 452, SIZE, font(13), (140, 140, 200))

    return bg

# ──────────────────────────────────────────────
# DISEÑO 2 — Azul rey · foto enmarcada · elegante geométrico
# Imagen: OldTown Hoi An
# ──────────────────────────────────────────────
ROYAL = (18, 52, 120)
GOLD  = (212, 175, 55)
WHITE = (255, 255, 255)

def design2_front():
    bg = Image.new("RGB", (SIZE, SIZE), ROYAL)
    draw = ImageDraw.Draw(bg)

    # Marco geométrico exterior
    draw.rectangle([(16, 16), (SIZE - 16, SIZE - 16)], outline=GOLD, width=2)
    draw.rectangle([(22, 22), (SIZE - 22, SIZE - 22)], outline=(255,255,255,80), width=1)

    # Foto enmarcada centrada arriba
    img = load_image(IMGS["B"])
    photo_size = 300
    photo = img.resize((photo_size, photo_size), Image.LANCZOS)
    # sutil viñeta sobre la foto
    vignette = Image.new("RGBA", (photo_size, photo_size), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    for i in range(30):
        alpha = int(120 * (i / 30))
        vd.rectangle([(i, i), (photo_size - i, photo_size - i)],
                     outline=(0, 0, 0, alpha), width=1)
    photo_rgba = photo.convert("RGBA")
    photo_rgba = Image.alpha_composite(photo_rgba, vignette)
    photo_x = (SIZE - photo_size) // 2
    bg.paste(photo_rgba.convert("RGB"), (photo_x, 38))

    # Borde dorado alrededor de la foto
    draw.rectangle([(photo_x - 2, 36), (photo_x + photo_size + 2, 38 + photo_size + 2)],
                   outline=GOLD, width=2)

    # Texto inferior
    draw.rectangle([(40, 360), (SIZE - 40, 362)], fill=GOLD)

    center_text(draw, "PHOTO TOURS", 372, SIZE, font(32), WHITE)
    center_text(draw, "HOI AN  ·  VIETNAM", 410, SIZE, font(16), GOLD)
    center_text(draw, "crismaturana.com", 446, SIZE, font(12), (180, 200, 240))

    # Esquinas decorativas
    for cx, cy, a1, a2 in [(28,28,0,0),(SIZE-28,28,1,0),(28,SIZE-28,0,1),(SIZE-28,SIZE-28,1,1)]:
        draw.line([(cx - (1-a1)*12, cy), (cx + a1*12, cy)], fill=GOLD, width=2)
        draw.line([(cx, cy - (1-a2)*12), (cx, cy + a2*12)], fill=GOLD, width=2)

    return bg

def design2_back():
    bg = Image.new("RGB", (SIZE, SIZE), ROYAL)
    draw = ImageDraw.Draw(bg)

    draw.rectangle([(16, 16), (SIZE - 16, SIZE - 16)], outline=GOLD, width=2)

    center_text(draw, "BOOK YOUR EXPERIENCE", 36, SIZE, font(16), GOLD)
    center_text(draw, "HOI AN · VIETNAM", 60, SIZE, font(12), (180, 200, 240))

    draw.rectangle([(60, 82), (SIZE - 60, 83)], fill=GOLD)

    qr = make_qr(WEBSITE, 190)
    # borde blanco alrededor del QR
    qr_frame = Image.new("RGB", (194, 194), GOLD)
    qr_frame.paste(qr, (2, 2))
    bg.paste(qr_frame, ((SIZE - 194) // 2, 94))

    draw.rectangle([(60, 300), (SIZE - 60, 301)], fill=GOLD)

    center_text(draw, "Scan to visit", 310, SIZE, font(13), (180, 200, 240))
    center_text(draw, "crismaturana.com", 332, SIZE, font(17), WHITE)

    center_text(draw, "Small group · Golden hour · Local access", 374, SIZE, font(12), (160, 180, 220))
    center_text(draw, "Dawn fishing markets · Lantern festivals", 394, SIZE, font(12), (160, 180, 220))
    center_text(draw, "Private & custom tours available", 414, SIZE, font(12), (160, 180, 220))

    draw.rectangle([(60, 442), (SIZE - 60, 443)], fill=(60, 80, 140))
    center_text(draw, "@crismaturanaphoto  ·  Est. 2022", 452, SIZE, font(12), (140, 160, 200))

    return bg

# ──────────────────────────────────────────────
# DISEÑO 3 — Foto dividida · split layout · minimalista oscuro
# Imagen: pescador con red (ThuBhon River)
# ──────────────────────────────────────────────
DARK  = (14, 14, 18)
MIST  = (200, 215, 230)
TERRA = (180, 120, 80)

def design3_front():
    base = Image.new("RGB", (SIZE, SIZE), DARK)
    img = load_image(IMGS["C"])

    # Foto ocupa mitad izquierda + desenfoque en borde derecho
    photo_w = 310
    photo = img.resize((photo_w, SIZE), Image.LANCZOS)

    # Máscara de desvanecimiento horizontal
    mask = Image.new("L", (photo_w, SIZE), 255)
    md = ImageDraw.Draw(mask)
    fade_start = 200
    for x in range(fade_start, photo_w):
        alpha = int(255 * (1 - (x - fade_start) / (photo_w - fade_start)))
        md.line([(x, 0), (x, SIZE)], fill=alpha)

    base.paste(photo, (0, 0), mask)

    draw = ImageDraw.Draw(base)

    # Panel derecho — textos
    rx = 290  # inicio zona texto

    # Línea vertical dorada separadora
    draw.rectangle([(rx - 2, 40), (rx - 1, SIZE - 40)], fill=TERRA)

    # Número grande decorativo
    draw.text((rx + 14, 30), "✦", font=font(18), fill=TERRA)

    center_x_right = rx + (SIZE - rx) // 2
    def right_center(text, y, fnt, color):
        bbox = draw.textbbox((0, 0), text, font=fnt)
        tw = bbox[2] - bbox[0]
        draw.text((center_x_right - tw // 2, y), text, font=fnt, fill=color)

    right_center("PHOTO", 75, font(34), WHITE)
    right_center("TOURS", 112, font(34), TERRA)

    draw.rectangle([(rx + 12, 155), (SIZE - 18, 157)], fill=TERRA)

    right_center("HOI AN", 168, font(19), MIST)
    right_center("VIETNAM", 194, font(13), (140, 155, 170))

    draw.rectangle([(rx + 12, 222), (SIZE - 18, 223)], fill=(40, 40, 50))

    # lines:
    for i, line in enumerate(["Small group", "Golden hour", "Real stories"]):
        right_center(line, 236 + i * 22, font(12), (160, 170, 185))

    right_center("crismaturana.com", 330, font(11), TERRA)

    # Esquina inferior izquierda — año
    draw.text((12, SIZE - 26), "© 2026", font=font(10), fill=(80, 80, 90))

    return base

def design3_back():
    base = Image.new("RGB", (SIZE, SIZE), DARK)
    draw = ImageDraw.Draw(base)

    # Patrón de puntos sutil
    for x in range(20, SIZE, 30):
        for y in range(20, SIZE, 30):
            draw.ellipse([(x-1, y-1),(x+1,y+1)], fill=(30, 30, 40))

    # Bloque superior
    draw.rectangle([(0, 0), (SIZE, 80)], fill=(20, 20, 28))
    center_text(draw, "PHOTO TOURS HOI AN", 18, SIZE, font(20), WHITE)
    center_text(draw, "VIETNAM  ·  crismaturana.com", 48, SIZE, font(12), TERRA)

    draw.rectangle([(0, 80), (SIZE, 83)], fill=TERRA)

    # QR centrado
    qr = make_qr(WEBSITE, 175)
    qr_bg = Image.new("RGB", (179, 179), WHITE)
    qr_bg.paste(qr, (2, 2))
    base.paste(qr_bg, ((SIZE - 179) // 2, 100))

    center_text(draw, "→  Scan to book your tour", 292, SIZE, font(13), MIST)

    draw.rectangle([(40, 325), (SIZE - 40, 326)], fill=(40, 40, 50))

    infos = [
        ("📍", "Hoi An, Vietnam"),
        ("🌅", "Dawn & dusk sessions"),
        ("👥", "Max 6 photographers"),
        ("📷", "All skill levels welcome"),
    ]
    for i, (icon, text) in enumerate(infos):
        y = 338 + i * 24
        draw.text((60, y), icon + "  " + text, font=font(12), fill=(160, 170, 185))

    draw.rectangle([(0, SIZE - 45), (SIZE, SIZE)], fill=(20, 20, 28))
    center_text(draw, "@crismaturanaphoto", SIZE - 30, SIZE, font(13), TERRA)

    return base

# ──────────────────────────────────────────────
# Guardar todo
# ──────────────────────────────────────────────
out = "/Users/matuguz/Documents/GitHub/crismaturanaphoto/flyers"
import os; os.makedirs(out, exist_ok=True)

print("Generando diseño 1...")
design1_front().save(f"{out}/flyer1_front.jpg", quality=95)
design1_back().save(f"{out}/flyer1_back.jpg", quality=95)
print("Generando diseño 2...")
design2_front().save(f"{out}/flyer2_front.jpg", quality=95)
design2_back().save(f"{out}/flyer2_back.jpg", quality=95)
print("Generando diseño 3...")
design3_front().save(f"{out}/flyer3_front.jpg", quality=95)
design3_back().save(f"{out}/flyer3_back.jpg", quality=95)

print("✓ 6 archivos guardados en /flyers/")
