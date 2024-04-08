import random
from src.letter import Letter


class Settings:
    def __init__(self, theme=1, lang=1):
        self.lang = lang
        self.dict = []
        self.theme = theme

    def load_dict(self):
        if self.lang:
            with open("assets/eng.txt", 'r') as eng:
                self.dict = eng.readlines()
        else:
            with open("assets/russian.txt", encoding='utf-8') as rus:
                self.dict = rus.readlines()

    def generate_text(self, window):
        text = []
        self.load_dict()
        for _ in range(int(window.words_button.count)):
            word = random.choice(self.dict).strip()
            for i in range(len(word)):
                letter = Letter(word[i], self.theme)
                text.append(letter)
            text.append(Letter('•', self.theme))
        text.pop(len(text) - 1)
        return text

