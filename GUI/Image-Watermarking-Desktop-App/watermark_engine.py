from PIL import Image, ImageDraw
class WaterMarkEngine:
    def image_watermark(self, image, text, position, opac, font, margin):
        if image:
            if text:
                img_w = image.width
                img_h = image.height
                draw = ImageDraw.Draw(image)
                bbox = draw.textbbox((0,0), text, font)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                x = img_w - tw
                y = img_h - th





