import pygame
import pygame_menu
import os
from pygame_menu import themes, Theme


pygame.init()
surface = pygame.display.set_mode((600, 400))
font = pygame_menu.font.FONT_MUNRO
mytheme = Theme(widget_font=font,
                background_color=(0, 0, 0, 0), # transparent background
                title_background_color=(4, 47, 126),
                title_font_shadow=True,
                widget_padding=25)


mainmenu = pygame_menu.Menu("You've lost", 600, 400, theme=mytheme)
mainmenu.add.button('Try again', start_the_game)
mainmenu.add.button('Quit lobby', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
mainmenu.mainloop(surface)