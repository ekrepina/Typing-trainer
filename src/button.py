import pygame

WORDS_DEPENDENCY = {5: 10, 10: 20, 20: 5}
START_WORD_COUNT = '5'


class ButtonTheme:
    def __init__(self, x, y, width, height, image=pygame.image.load("assets/dark_button.png")):
        self.theme = 1
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_button(self, window):
        window.screen.blit(self.image, (self.x, self.y))

    def is_pressed(self, window):
        pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            self.theme = not self.theme
            window.dict_button.theme = not window.dict_button.theme
            window.settings.theme = not window.settings.theme
            window.words_button.theme = not window.words_button.theme
            window.update_text()
            window.words_button.change_color()

        if self.theme:
            self.image = pygame.image.load("assets/dark_button.png")
        else:
            self.image = pygame.image.load("assets/light_button.png")


class ButtonDict:

    def __init__(self, x, y, width, height, lang="rus"):
        self.theme = 1
        self.lang = lang
        self.text = pygame.font.Font("assets/font.ttf", 15).render(self.lang, True, (0, 0, 0))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0, 0, 0)

    def draw_button(self, window):
        window.screen.blit(self.text, self.text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2)))

    def is_pressed(self, window):
        pos = pygame.mouse.get_pos()

        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            window.settings.lang = not window.settings.lang
            self.change_lang()
            window.text = window.settings.generate_text(window)

        font = pygame.font.Font("assets/font.ttf", 15)
        self.change_color()
        self.text = font.render(self.lang, True, self.color)

    def change_lang(self):
        if self.lang == "rus":
            self.lang = "eng"
        else:
            self.lang = "rus"

    def change_color(self):
        if self.theme:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)


class ButtonWordCount:

    def __init__(self, x, y, width, height):
        self.theme = 1
        self.count = START_WORD_COUNT
        self.text = pygame.font.Font("assets/font.ttf", 15).render(self.count, True, (0, 0, 0))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0, 0, 0)

    def draw_button(self, window):
        window.screen.blit(self.text, self.text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2)))

    def is_pressed(self, window):
        pos = pygame.mouse.get_pos()

        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            self.change_count()
            window.text = window.settings.generate_text(window)

        font = pygame.font.Font("assets/font.ttf", 15)
        self.change_color()
        self.text = font.render(self.count, True, self.color)

    def change_count(self):
        self.count = str(WORDS_DEPENDENCY[int(self.count)])

    def change_color(self):
        if self.theme:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)