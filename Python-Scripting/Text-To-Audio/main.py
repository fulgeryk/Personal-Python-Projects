from pypdf import PdfReader
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tts_engine import ENGINE
from pathlib import Path

MAX_CHARS = 2500
engine = ENGINE()
output_dir = "output"
engine.list_voices()
while True:
    try:
        choose = int(input("Your choose: "))
    except ValueError:
        print("Please enter a number")
        continue
    if 0 <= choose < len(engine.voices):
        break
engine.set_voice(choose)
engine.select_rate(100)
engine.select_volume(1)
filetypes = (
    ('PDF files', '*.pdf'),
    ('All files', '*.*'),
)
Tk().withdraw()
filmename = askopenfilename(title='Select a file... ', filetypes=filetypes)
reader = PdfReader(filmename)
path = Path.cwd() / output_dir
try:
    path.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    print("Folder is already there")
else:
    print("Folder was created")
for i in range(len(reader.pages)):
    text = reader.pages[i].extract_text()
    if not text:
        continue
    text = text.strip().replace("\n", " ")
    for chunk_index, start in enumerate(range(0,len(text), MAX_CHARS), start=1):
        chunk = text[start:start + MAX_CHARS]
        filepath = path / f"page_{i+1:03}_chunk_{chunk_index:02}.wav"
        print(f"Processing page {i + 1}/{len(reader.pages)} - chunk {chunk_index}")
        engine.queue_save(chunk, filepath)
    print(f"Generating audio for page {i + 1}...")
    engine.flush()
