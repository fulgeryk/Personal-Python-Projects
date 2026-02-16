import numpy as np
from PIL import Image

class ProcessImage:
    def __init__(self):
        self.image = None

    def process_image(self, image: str):
        self.image = np.array(Image.open(image))
        x,y,z =self.image.shape
        self.image = self.image.reshape(x*y,z)
        total_pixels = x*y
        step = 32
        map_color = {}
        for pixel in self.image:
            pixel = tuple(pixel)
            pixel_quantized = (
                (pixel[0] // step) * step,
                (pixel[1] // step) * step,
                (pixel[2] // step) * step
            )
            if pixel_quantized in map_color:
                map_color[pixel_quantized] = map_color[pixel_quantized] + 1
            else:
                map_color[pixel_quantized] = 1
        list_top_colors = []
        for i in range(10):
            max_count = 0
            max_color = None
            for color,count in map_color.items():
                if count > max_count:
                    max_count = count
                    max_color = color
            percent = max_count / total_pixels * 100
            percent = round(percent, 2)
            list_top_colors.append([max_color, max_count, percent])
            map_color.pop(max_color, None)
        return list_top_colors


