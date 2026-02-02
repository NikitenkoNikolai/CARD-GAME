import pygame
from data_main_menu import DataMainMenu, DataSettings, DataSettingsAudio, DataSettingsVideo, DataSettingsText

from data_childhood import *
from data_mini_menu import DataMiniMenu


class View:
    def __init__(self):
        pygame.init()
        self.__width_display, self.__height_display = StandardFunctionality.window_size()
        self.__display_window = pygame.display.set_mode((self.__width_display, self.__height_display))

    def main_menu(self):
        background = pygame.image.load(DataMainMenu().get_background_img())
        start_pos_open_background = (0, 0)
        self.__display_window.blit(background, start_pos_open_background)
        for btn in DataMainMenu().buttons():
            btn.draw(self.__display_window)
        pygame.display.flip()

    def settings(self):
        background = pygame.image.load(DataSettings().get_background_img())
        start_pos_open_background = (0, 0)
        self.__display_window.blit(background, start_pos_open_background)
        for btn in DataSettings().buttons():
            btn.draw(self.__display_window)
        pygame.display.flip()

    def settings_audio(self, pos_point_x=None, name_point=None):
        background = pygame.image.load(DataSettingsAudio().get_background_img())
        start_pos_open_background = (0, 0)
        self.__display_window.blit(background, start_pos_open_background)
        for slider in DataSettingsAudio().sliders():
            slider.draw(self.__display_window, pos_point_x, name_point)
        for btn in DataSettingsAudio().buttons():
            btn.draw(self.__display_window)
        pygame.display.flip()

    def settings_video(self):
        background = pygame.image.load(DataSettingsAudio().get_background_img())
        start_pos_open_background = (0, 0)
        self.__display_window.blit(background, start_pos_open_background)
        for select_box in DataSettingsVideo().select_box():
            select_box.draw(self.__display_window)
        for btn in DataSettingsVideo().buttons():
            btn.draw(self.__display_window)
        pygame.display.flip()

    def settings_text(self):
        background = pygame.image.load(DataSettingsText().get_background_img())
        start_pos_open_background = (0, 0)
        self.__display_window.blit(background, start_pos_open_background)
        for btn in DataSettingsText().buttons():
            btn.draw(self.__display_window)
        pygame.display.flip()

    def childhood_level(self, menu=False):
        number_card = -1
        background = pygame.image.load(DataChildHoodInterface().get_background_img())
        start_pos_open_background = (0, 0)
        self.__display_window.blit(background, start_pos_open_background)

        if menu:
            mini_menu = DataMiniMenu()
            mini_menu.draw_background(self.__display_window)
            for btn in mini_menu.buttons():
                btn.draw(self.__display_window)
        else:
            for stat in DataChildHoodInterface().stats():
                stat.draw(self.__display_window)

            for enemy in DataChildhoodEnemy().enemy():
                enemy.draw(self.__display_window)

            for card in DataChildhoodUserCards().cards_user():
                number_card += 1
                if type(card) != int:
                    method_card = card[0]
                    method_card.take_pos_x_card(number_card)
                    method_card.draw(self.__display_window, number_card)

            for btn in DataChildHoodInterface().buttons():
                btn.draw(self.__display_window)

        pygame.display.flip()
