from process_explorer import StandardFunctionality
from color import Colors
import pygame


class Enemy:
    def __init__(self, img_path=None):
        self._width_display, self._height_display = StandardFunctionality.window_size()
        self._width_enemy, self._height_enemy = self._width_display // 2.7, self._height_display // 1.8
        self._img = None
        self._img_path = img_path
        self.__pos_x = self.get_center_position(self._width_display, self._width_enemy)
        self.__pos_y = self._height_display // 10

    @staticmethod
    def get_center_position(width_display, width_rect):
        return width_display / 2 - width_rect / 2

    def get_info_rect_enemy(self):

        return pygame.Rect(self.__pos_x, self.__pos_y, self._width_enemy, self._height_enemy)

    def get_info_size_enemy(self):
        return [self._width_enemy, self._height_enemy]

    def get_info_status_screen(self):
        if not self._img_path:
            self._img = None
            return self._img
        self._img = pygame.image.load(self._img_path)
        self._img = pygame.transform.scale(self._img, (self._width_enemy, self._height_enemy))
        return self._img

    def draw(self, display_window):
        self._img = self.get_info_status_screen()
        white = Colors.white()
        red = Colors.red()
        if self._img:
            rect = self._img.get_rect(topleft=(self.__pos_x, self.__pos_y))
            current_img = self._img
            display_window.blit(current_img, rect.topleft)
        else:
            pygame.draw.rect(display_window, red, (self.__pos_x, self.__pos_y, self._width_enemy, self._height_enemy))
