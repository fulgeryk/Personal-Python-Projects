from tkinter import *
from PIL import Image, ImageTk
from engine import Engine

THEME_COLOR = "#FFFFFF"
reps = 0
timer = 0

class TypingSpeedInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.geometry("1024x648")
        self.window.grid_rowconfigure(0, weight=15)
        self.window.grid_rowconfigure(1, weight=15)
        self.window.grid_rowconfigure(2, weight=15)
        self.window.grid_rowconfigure(3, weight=15)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.start_image = Image.open("./images/start.png")
        self.start_image = self.start_image.resize((200, 150))
        self.start_image = ImageTk.PhotoImage(image=self.start_image)
        self.start_button = Button(
            image=self.start_image,
            compound="top",
            highlightthickness=0,
            relief="flat",
            borderwidth=0,
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            command=self.start_pressed
        )
        self.start_button.grid(row=3, column=0, sticky="w")
        self.reset_image = Image.open("./images/reset.png")
        self.reset_image = self.reset_image.resize((200,150))
        self.reset_image = ImageTk.PhotoImage(image=self.reset_image)
        self.reset_button = Button(
            image=self.reset_image,
            compound = "top",
            highlightthickness = 0,
            relief = "flat",
            borderwidth = 0,
            bg = THEME_COLOR,
            activebackground = THEME_COLOR,
            command=self.reset
        )
        self.reset_button.grid(row=3, column=2,sticky="e")
        self.target_label = Label(
            text="Press Start to begin...",
            anchor= CENTER,
            bg=THEME_COLOR,
            wraplength=700,
            height=6,
            justify="center",
            font=("Arial", 16, "bold"),
            cursor="hand2",
            fg="black"
        )
        self.target_label.grid(row=0, column=0, columnspan=3, sticky="n",pady=(120,0))
        self.input_entry=Entry(font=('calibre',10,'normal'))
        self.input_entry.grid(row = 1, column=0, columnspan=3, pady=(60,0), sticky="n")
        self.input_entry.bind("<space>", self.on_space)
        self.frame = Frame(bg=THEME_COLOR, pady=5)
        self.frame.grid(row=2, columnspan=3, sticky="n")
        self.time_label = Label(self.frame, text="Time: 0s")
        self.time_label.pack(pady=2)
        self.wpm_label = Label(self.frame,text="WPM: 0")
        self.wpm_label.pack(pady=2)
        self.accuracy_label = Label(self.frame,text="Accuracy: 0")
        self.accuracy_label.pack(pady=2)
        self.seconds = 0
        self.timer_running = False
        self.engine = Engine()
        self.total_words = 0
        self.correct_words = 0
        self.window.mainloop()

# -------------------- TIMER --------------- #
    def start_timer(self):
        if self.timer_running != True:
            self.timer_running = True
            self.tick()

    def tick(self):
        if not self.timer_running:
            return
        else:
            self.seconds += 1
            self.time_label.config(text=f"Time: {self.seconds}s")
            self.window.after(1000,self.tick)

    def reset(self):
        self.correct_words = 0
        self.total_words = 0
        self.wpm_label.config(text=f"WPM :0")
        self.accuracy_label.config(text=f"Accuracy: 0")
        self.timer_running = False
        self.seconds = 0
        self.time_label.config(text=f"Time: {self.seconds}s")
        self.input_entry.delete(0, 'end')
        self.target_label.config(text="Press Start to begin...")
        self.engine.words = []
        self.engine.current_index = 0

    def start_pressed(self):
        self.correct_words = 0
        self.total_words = 0
        self.wpm_label.config(text=f"WPM :0")
        self.accuracy_label.config(text=f"Accuracy: 0")
        self.engine.load_text(
            "The quick brown fox jumps over the lazy dog. "
            "Typing fast requires focus, accuracy, and steady rhythm. "
            "Practice every day to improve your speed and confidence."
        )
        self.target_label.config(text=self.engine.text)
        self.seconds = 0
        self.start_timer()
        self.input_entry.delete(0, 'end')
        self.input_entry.focus()

    def on_space(self, event):
        print("SPACE pressed")
        if not self.engine.words:
            return "break"
        typed_word = self.input_entry.get()
        typed_word = typed_word.strip()
        if not typed_word:
            return "break"
        is_correct, finished = self.engine.submit_word(typed_word)
        self.total_words += 1
        if is_correct:
            self.correct_words +=1
        accuracy = self.correct_words / self.total_words * 100
        self.accuracy_label.config(text=f"Accuracy: {round(accuracy, 1)}")
        if self.seconds > 0:
            wpm = (self.correct_words * 60) / self.seconds
            self.wpm_label.config(text=f"WPM: {round(wpm)}")
        self.input_entry.delete(0,'end')
        if finished:
            self.timer_running = False
        return "break"



