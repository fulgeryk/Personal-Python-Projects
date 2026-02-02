import string

class Engine:
    def __init__(self):
        self.text = ""
        self.words = []
        self.current_index = 0


    def load_text(self, text: str):
        self.text = text
        self.words = self.text.split()
        self.current_index = 0

    def submit_word(self, typed_word: str):
        finished = False
        correct_word = self.words[self.current_index]
        typed_norm = self.normalize(typed_word)
        correct_norm = self.normalize(correct_word)
        is_correct = typed_norm == correct_norm
        self.current_index += 1
        if self.current_index >= len(self.words):
            finished = True
        return is_correct, finished

    def normalize(self, word):
        new_word = word.strip(string.punctuation)
        new_word = new_word.lower()
        return new_word



