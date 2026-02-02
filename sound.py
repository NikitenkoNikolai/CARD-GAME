import pygame
from data_base import SavesSettings


class Sounds:
    def __init__(self):
        self.__volume_all, self.__volume_music, self.__volume_effects = self.get_info_audio()
        if self.__volume_music > self.__volume_all:
            self.__volume_music = self.__volume_all
        if self.__volume_effects > self.__volume_all:
            self.__volume_effects = self.__volume_all

    def get_volume_all(self):
        return self.__volume_all

    def get_volume_music(self):
        return self.__volume_music

    def get_volume_effects(self):
        return self.__volume_effects

    @staticmethod
    def get_info_audio():
        columns = {'audio_all': 0, 'audio_music': 1, 'audio_effects': 2}
        values = SavesSettings().get_data_settings()
        volume_all = (float(values[columns['audio_all']]) + 5) / 100
        volume_music = (float(values[columns['audio_music']]) + 5) / 100 - 0.01
        volume_effects = (float(values[columns['audio_effects']]) + 5) / 100
        return [volume_all, volume_music, volume_effects]


class Music(Sounds):
    @staticmethod
    def start_play_music(status_game_last, status_game_now):
        if status_game_last != status_game_now:
            if status_game_now == 'MainMenu' and (status_game_last == 'IsPlaying' or not status_game_last):
                Music().start_bg_music_main_menu()
            elif status_game_now == 'IsPlaying' and status_game_last == 'MainMenu':
                Music().start_play_game_music()

    @staticmethod
    def start_play_game_music(status_mode='StoryMode'):
        if status_mode == 'StoryMode':
            Music.start_bg_music_childhood()

    @staticmethod
    def start_bg_music_childhood():
        pygame.mixer.music.load('audio/Childhood.mp3')
        pygame.mixer.music.play(-1)

    @staticmethod
    def start_bg_music_main_menu():
        pygame.mixer.music.load('audio/Main_menu.mp3')
        pygame.mixer.music.play(-1)

    @staticmethod
    def set_new_volume_music():
        pygame.mixer.music.set_volume(Sounds().get_volume_music())


class PressButton(Sounds):
    @staticmethod
    def press_wood_button():
        wood_button = pygame.mixer.Sound('audio/wood_button.mp3')
        wood_button.set_volume(Sounds().get_volume_effects())
        wood_button.play()
