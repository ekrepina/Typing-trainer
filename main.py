import pygame
import sys

from src.window import Window

window = Window()
window.draw()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                window.generate_text()
                window.draw()
            else:
                window.input_text()
        if event.type == pygame.MOUSEBUTTONUP:
            window.theme_button.is_pressed(window)
            window.dict_button.is_pressed(window)
            window.words_button.is_pressed(window)
            window.draw()
