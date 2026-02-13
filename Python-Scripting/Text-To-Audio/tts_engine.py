import pyttsx3

class ENGINE:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('volume', 0.35)
        self.choose = None

    def select_rate(self, rate):
        self.engine.setProperty('rate', rate)

    def select_volume(self,volume):
        self.engine.setProperty('volume', volume)


    def list_voices(self):
        for index, voice in enumerate(self.voices):
            print(f" Choose {index} for: \n Name: {voice.name} \n Languages: {voice.languages} \n Gender: {voice.gender} \n Age: {voice.age}")

    def set_voice(self, index):
        self.engine.setProperty("voice", self.voices[index].id)

    def queue_save(self, text, output_path):
        self.engine.save_to_file(text, str(output_path))

    def flush(self):
        self.engine.runAndWait()






