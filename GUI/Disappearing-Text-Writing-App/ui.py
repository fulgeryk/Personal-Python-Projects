import tkinter.scrolledtext
from tkinter import *
from engine import Engine
THEME_COLOR = "#FFFFFF"
class DissappearingTextUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dissapearing Text Writing")
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)
        self.window.geometry("800x500")
        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=0)
        self.window.grid_columnconfigure(0, weight=1)
        self.title_label = Label(
            text="Dissapearing Text Writing",
            anchor = CENTER,
            bg = THEME_COLOR,
            wraplength = 700,
            justify = "center",
            font = ("Arial", 16, "bold"),
            cursor = "hand2",
            fg = "black"
        )
        self.title_label.grid(row=0, column=0, sticky="nsew")
        self.text_scroll = tkinter.scrolledtext.ScrolledText(
            self.window,
            wrap = WORD,
            width=60,
            height=10,
            font = ("Times New Roman",
                    15)
        )
        self.text_scroll.grid(row=1, column=0, sticky="nsew")
        self.text_scroll.focus()
        self.text_scroll.bind("<KeyRelease>", self.start_typing)
        self.status_label = Label(
            text="Waiting...",
            anchor=CENTER,
            bg=THEME_COLOR,
            wraplength=700,
            justify="center",
            font=("Arial", 16, "bold"),
            cursor="hand2",
            fg="#FF0000"
        )
        self.status_label.grid(row=2, column=0, sticky="nsew")
        self.engine = Engine()
        self.update_countdown()
        self.window.mainloop()



    def start_typing(self, event):
        self.status_label.config(text="Typing...",fg="#008000")
        self.engine.on_activity()

    def clear_text(self):
        self.text_scroll.delete(1.0, "end-1c")
        self.status_label.config(text="Waiting...",fg="#FF0000")
        self.text_scroll.focus()

    def update_countdown(self):
        remaining, expired = self.engine.tick()
        if remaining is None:
            self.status_label.config(text="Waiting...", fg="#FF0000")
        else:
            self.status_label.config(text=f"Disappears in {remaining}")
        if expired:
            self.clear_text()
        self.window.after(1000, self.update_countdown)