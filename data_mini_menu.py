from process_explorer import StandardFunctionality
from button import Button
import pygame


class DataMiniMenu:
    def __init__(self):
        self.__background = f'images/MiniMenu.jpg'
        self.__button_img = 'images/Button.jpg'
        self.__width_display, self.__height_display = StandardFunctionality.window_size()
        self.__width_display //= 2
        self.__height_display //= 2
        self.__width_display_mini_menu = self.__width_display // 2
        self.__height_display_mini_menu = self.__height_display // 2

    def background_img(self):
        return self.__background

    def draw_background(self, display_window):
        img = pygame.image.load(self.__background)
        img = pygame.transform.scale(img, (self.__width_display, self.__height_display))
        rect = img.get_rect(topleft=(self.__width_display_mini_menu, self.__height_display_mini_menu))
        current_img = img
        display_window.blit(current_img, rect.topleft)

    def buttons(self):
        WIDTH_BUTTON_CONST = self.__width_display // 2
        HEIGHT_BUTTON_CONST = self.__height_display // 8
        position_continue = (self.__width_display - WIDTH_BUTTON_CONST // 2,
                             self.__height_display_mini_menu * 5 / 3.5)
        position_settings = (self.__width_display - WIDTH_BUTTON_CONST // 2,
                             self.__height_display_mini_menu * 6.5 / 3.5)
        position_main_menu = (self.__width_display - WIDTH_BUTTON_CONST // 2,
                              self.__height_display_mini_menu * 8 / 3.5)
        size = (WIDTH_BUTTON_CONST, HEIGHT_BUTTON_CONST)

        continue_button = Button(position_continue, size, text='Continue', name='continue_playing',
                                 img_path=self.__button_img)
        settings_button = Button(position_settings, size, text='Settings', name='settings', img_path=self.__button_img)
        main_menu_button = Button(position_main_menu, size, text='Main menu', name='main_menu',
                                  img_path=self.__button_img)
        main_menu_buttons = [continue_button, settings_button, main_menu_button]
        return main_menu_buttons
