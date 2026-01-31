from PIL import Image, ImageDraw
class WaterMarkEngine:
    def image_watermark(self, image, text, opac, font, margin):
        if not image or not text:
            return image

        img = image.copy()
        base = img.convert("RGBA")
        overlay = Image.new("RGBA", base.size, (0,0,0,0))
        draw = ImageDraw.Draw(overlay)
        draw_w, draw_h = base.size
        bbox = draw.textbbox((0,0), text, font = font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = draw_w - tw - margin
        y = draw_h - th - margin
        alpha = int(opac/100 * 255)
        draw.text((100,100), text=text, font=font, fill=(0,0,0,alpha))
        result = Image.alpha_composite(base, overlay)
        return result
