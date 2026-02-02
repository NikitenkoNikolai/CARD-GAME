from transmitter import TransmitterStatusGame
from process_explorer import StandardFunctionality
from View import View
import pygame
from sound import Music
import doctest
pygame.init()


class Controller:
    def __init__(self, view_mod, model_mod):
        self.__view = view_mod
        self.__model = model_mod

    def run(self):
        status_game_last = False
        while True:

            status_game_now = TransmitterStatusGame(self.__view, self.__model)
            Music.start_play_music(status_game_last, status_game_now.get_status_game())
            status_game_last = status_game_now.get_status_game()
            Music().set_new_volume_music()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    StandardFunctionality.quit_game()
                TransmitterStatusGame(self.__view, self.__model).check_status_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    TransmitterStatusGame(self.__view, self.__model).check_status_game_mouse_press()


if __name__ == '__main__':
    doctest.testmod()
    view = View()
    game_model = StandardFunctionality()
    controller = Controller(view, game_model)
    controller.run()
