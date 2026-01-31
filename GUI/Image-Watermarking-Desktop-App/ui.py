from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFont
from watermark_engine import WaterMarkEngine
THEME_COLOR ="#FFFFFF"
engine = WaterMarkEngine()

class WatermarkInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Watermarking Desktop App")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        self.window.geometry("1024x648")
        self.window.grid_rowconfigure(0, weight=15)
        self.window.grid_rowconfigure(1, weight=15)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.upload_image = Image.open("./images/upload_button.png")
        self.upload_image = self.upload_image.resize((200,150))
        self.upload_image = ImageTk.PhotoImage(image=self.upload_image)
        self.upload_button = Button(
            image=self.upload_image,
            compound="top",  # text sub imagine
            highlightthickness=0,
            relief="flat",
            borderwidth = 0,
            bg = THEME_COLOR,
            activebackground = THEME_COLOR,
            command = self.file_open
        )
        self.upload_button.grid(row=2, column=0, sticky="s")
        self.path_label = Label(text="No file selected")
        self.path_label.grid(row=2, column=0, pady=(100,0))
        self.save_image = Image.open("./images/download_button.png")
        self.save_image = self.save_image.resize((200,150))
        self.save_image = ImageTk.PhotoImage(image=self.save_image)
        self.save_button = Button(
            image=self.save_image,
            compound="top",  # text sub imagine
            highlightthickness=0,
            relief="flat",
            borderwidth = 0,
            bg = THEME_COLOR,
            activebackground = THEME_COLOR,
            command=self.save_file
        )
        self.save_button.grid(row=2, column=1, sticky="s")
        self.image_path = ""
        self.preview_image = ""
        self.image_pillow = ""
        self.save_watermark = Entry(width=25)
        self.save_watermark.grid(row=2, column=0, pady=(0,60), padx=(20,0))
        self.canvas=Canvas(width=800,height=400, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=0, columnspan=2, rowspan=2)
        self.window.mainloop()

    def file_open(self):
        print("clicked")
        filePath = askopenfilename(initialdir = 'C:/', title="Select a File", filetypes=(("Photo Type", ".png"), ("All Files", "*.*")))
        if filePath:
            self.image_path = filePath
            self.path_label.config(text=self.image_path)
            self.preview(self.image_path)

    def preview(self, path):
        if path:
            box_w = 800
            box_h = 400
            self.preview_image = Image.open(path)
            self.image_pillow = self.preview_image
            img_w = self.preview_image.width
            img_h = self.preview_image.height
            scale_w = box_w / img_w
            scale_h = box_h / img_h
            scale = min(scale_w, scale_h)
            new_w = int(img_w * scale)
            new_h = int(img_h * scale)
            self.preview_image = self.preview_image.resize((new_w, new_h))
            self.preview_image = ImageTk.PhotoImage(self.preview_image)
            self.canvas.delete("all")
            self.canvas.create_image(400, 200, image = self.preview_image, anchor = "center")

    def save_file(self):
        if self.image_pillow:
            path = asksaveasfilename(filetypes=((".png", ".png"), ("All Files", "*.*")), defaultextension=".png", confirmoverwrite=False)
            if path:
                save_text = self.save_watermark.get()
                if save_text:
                    watermarked = engine.image_watermark(
                        image=self.image_pillow.copy(),
                        text=save_text,
                        opac=100,
                        font = ImageFont.truetype("arial.ttf", 150),
                        margin=20
                    )
                    watermarked.save(path)









