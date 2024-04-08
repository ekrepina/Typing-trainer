import pygame
from src.button import Theme
from src.button import Dict
from src.button import WordCount
from src.settings import Settings
from src.statistics import Statistics
import time

letters = {'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[',
           'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';',
           'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': 't'}


class Window:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Typing Trainer")
        self.screen = pygame.display.set_mode((800, 492))
        self.settings = Settings()
        self.text = []
        self.statistics = Statistics()
        self.theme_button = Theme(10, 10, 30, 30)
        self.dict_button = Dict(10, 50, 30, 30)
        self.words_button = WordCount(10, 90, 30, 30)

    def draw(self):
        if self.settings.theme == 1:
            self.screen.blit(pygame.image.load("assets/light_theme.png"), (0, 0))
        else:
            self.screen.blit(pygame.image.load("assets/dark_theme.png"), (0, 0))
        self.draw_start_text()
        self.draw_text()
        self.theme_button.draw_button(self)
        self.dict_button.draw_button(self)
        self.words_button.draw_button(self)
        pygame.display.update()

    def draw_start_text(self):
        font = pygame.font.Font("assets/font.ttf", 40)
        if self.settings.theme:
            color = (0, 0, 0)
        else:
            color = (255, 255, 255)
        text = font.render("Typing trainer", True, color)
        pos = (400, 50)
        place = text.get_rect(center=pos)
        self.screen.blit(text, place)
        font = pygame.font.Font("assets/font.ttf", 15)
        text = font.render("press ENTER to generate text", True, color)
        pos = (400, 100)
        place = text.get_rect(center=pos)
        self.screen.blit(text, place)
        text = font.render("press SPACE to start typing", True, color)
        pos = (400, 120)
        place = text.get_rect(center=pos)
        self.screen.blit(text, place)

    def draw_text(self):
        font = pygame.font.Font("assets/font.ttf", 25)
        pos = (80, 200)
        for i in range(len(self.text)):
            text = font.render(self.text[i].letter, True, self.text[i].color)
            if pos[0] > 650 and self.text[i].letter == '•':
                pos = (80, pos[1] + 25)
            else:
                pos = (pos[0] + 14, pos[1])
            # pos = (pos[0] + 14, pos[1])
            place = text.get_rect(center=pos)
            self.screen.blit(text, place)

    def draw_statistics(self):
        font = pygame.font.Font("assets/font.ttf", 15)
        if self.settings.theme:
            color = (0, 0, 0)
        else:
            color = (255, 255, 255)
        text = font.render("WPM: " + str(self.statistics.wpm), True, color)
        pos = (350, 400)
        place = text.get_rect(center=pos)
        self.screen.blit(text, place)
        text = font.render("Errors: " + str(self.statistics.errors_count), True, color)
        pos = (450, 400)
        place = text.get_rect(center=pos)
        self.screen.blit(text, place)

    def input_text(self):
        start = time.time()
        for i in range(len(self.text)):
            try_count = 1
            flag = self.check_key(self.text[i])
            while not flag[1]:
                if flag[0]:
                    try_count += 1
                flag = self.check_key(self.text[i])
            if try_count != 1:
                self.text[i].color = (255, 0, 0)
            else:
                self.text[i].color = (112, 112, 112)
            self.draw()
            pygame.display.update()
        end = time.time()
        self.statistics.time = end - start
        self.statistics.update_wpm(self)
        self.draw()
        self.draw_statistics()
        pygame.display.update()

    def check_key(self, cur_letter):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.name(event.key)
                if pressed_key == 'space':
                    pressed_key = '•'
                if pressed_key == cur_letter.letter:
                    return True, True
                if cur_letter.letter in letters and letters[cur_letter.letter] == pressed_key:
                    return True, True
                self.statistics.errors_count += 1
                return True, False
        return False, False

    def generate_text(self):
        self.text = self.settings.generate_text(self)

    def update_text(self):
        for i in range(len(self.text)):
            if self.settings.theme:
                self.text[i].color = (0, 0, 0)
            else:
                self.text[i].color = (255, 255, 255)
