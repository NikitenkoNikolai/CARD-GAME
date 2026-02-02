from GameModel import MainMenu, Settings, SettingsAudio, SettingsVideo, SettingsText, ChildHood
from data_base import SavesSettings


class TransmitterStatusGame:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__status_game = SavesSettings().get_data_game_status()

    def get_status_game(self):
        return self.__status_game

    def create_status_game(self, new_status):
        SavesSettings().save_data_game_status(new_status)
        self.__status_game = self.get_status_game()

    def check_status_game(self):
        if self.__status_game == 'IsPlaying':
            ChildHood(self.__view, self.__model).open()
        else:
            if self.__status_game == 'MainMenu':
                self.__status_game = 'MainMenu'
                MainMenu(self.__view, self.__model).open()
            elif self.__status_game == 'Settings':
                self.__status_game = 'Settings'
                Settings(self.__view, self.__model).open()
            elif self.__status_game == 'SettingsAudio':
                self.__status_game = 'SettingsAudio'
                SettingsAudio(self.__view, self.__model).open()
            elif self.__status_game == 'SettingsVideo':
                self.__status_game = 'SettingsVideo'
                SettingsVideo(self.__view, self.__model).open()
            elif self.__status_game == 'SettingsText':
                self.__status_game = 'SettingsText'
                SettingsText(self.__view, self.__model).open()

    def check_status_game_mouse_press(self):
        if self.__status_game == 'IsPlaying':
            ChildHood(self.__view, self.__model).check_press_mouse()
        else:
            if self.__status_game == 'MainMenu':
                MainMenu(self.__view, self.__model).check_press_mouse()
            elif self.__status_game == 'Settings':
                Settings(self.__view, self.__model).check_press_mouse()
            elif self.__status_game == 'SettingsAudio':
                SettingsAudio(self.__view, self.__model).check_press_mouse()
            elif self.__status_game == 'SettingsVideo':
                SettingsVideo(self.__view, self.__model).check_press_mouse()
            elif self.__status_game == 'SettingsText':
                SettingsText(self.__view, self.__model).check_press_mouse()
