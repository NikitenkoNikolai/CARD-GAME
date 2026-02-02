# import datetime

from math import log, ceil
from button import *
from data_base import SavesSettings, SavesGameAndMode, SavesDeckAndCardsUser, SavesDeckAndCardsEnemy, SavesStatsUser, \
    SavesStatsEnemy
from data_main_menu import DataMainMenu, DataSettings, DataSettingsAudio, DataSettingsVideo, DataSettingsText
from data_childhood import *
from data_mini_menu import DataMiniMenu
from game_interface import LogicCardField
from segment_tree import SegmentTree
from deck_and_cards_childhood import Deck, CardsOnHand
from enemy_logics import EnemyMove
from sound import PressButton
import pygame

pygame.init()


class ModulesOpponents:
    @staticmethod
    def get_module_opponent():
        turn = SavesGameAndMode().get_turn()
        if turn == 'user':
            return SavesDeckAndCardsUser
        else:
            return SavesDeckAndCardsEnemy


class SettingsAudio:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def open(self, pos_point_x=None, name_point=None):
        SavesSettings().save_data_game_status('SettingsAudio')
        self.__view.settings_audio(pos_point_x, name_point)

    def check_press_mouse(self):
        x, y = pygame.mouse.get_pos()
        for slider in DataSettingsAudio().sliders():
            if slider.get_info_rect_bond().collidepoint(x, y):
                slider_y_border_up = slider.get_info_rect_bond()[1]
                slider_y_border_down = slider.get_info_rect_bond()[1] + slider.get_info_rect_bond()[3]
                slider_x_border_left = slider.get_info_rect_bond()[0]
                slider_x_border_right = slider.get_info_rect_bond()[0] + slider.get_info_rect_bond()[2]
                if slider_y_border_up <= y <= slider_y_border_down:
                    if slider_x_border_left <= x <= slider_x_border_right:
                        center_point = x - slider.get_info_point()[3] // 2.6
                        name_point = slider.get_info_point()[-1]
                        SettingsAudio(self.__view, self.__model).open(pos_point_x=center_point,
                                                                      name_point=name_point)

        for btn in DataSettingsAudio().buttons():
            if btn.get_info_rect_button().collidepoint(x, y):
                if btn.get_info_button()[-1] == 'back':
                    PressButton.press_wood_button()
                    Settings(self.__view, self.__model).open()


class SettingsVideo:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def open(self, screen_mode=None, screen_mode_save=False):
        SavesSettings().save_data_game_status('SettingsVideo')
        if screen_mode:
            SavesSettings().save_status_screen(screen_mode)
        if screen_mode_save:
            SavesSettings().save_settings_info_video()
        self.__view.settings_video()

    def check_press_mouse(self):
        x, y = pygame.mouse.get_pos()

        for select_box in DataSettingsVideo().select_box():
            if select_box.get_info_rect_button().collidepoint(x, y):
                if select_box.get_info_button()[-1] == 'full_screen_box':
                    PressButton.press_wood_button()
                    SettingsVideo(self.__view, self.__model).open(screen_mode='full_screen_box')
                if select_box.get_info_button()[-1] == 'window_screen_box':
                    PressButton.press_wood_button()
                    SettingsVideo(self.__view, self.__model).open(screen_mode='window_screen_box')

        for btn in DataSettingsVideo().buttons():
            if btn.get_info_rect_button().collidepoint(x, y):
                if btn.get_info_button()[-1] == 'save':
                    PressButton.press_wood_button()
                    SettingsVideo(self.__view, self.__model).open(screen_mode_save=True)
                if btn.get_info_button()[-1] == 'back':
                    PressButton.press_wood_button()
                    columns = {'full_screen_box': 3, 'window_screen_box': 4, 'full_screen': 5, 'window_screen': 6}
                    values = SavesSettings().get_data_settings()
                    SavesSettings().save_data_settings('full_screen_box', values[columns['full_screen']])
                    SavesSettings().save_data_settings('window_screen_box', values[columns['window_screen']])
                    Settings(self.__view, self.__model).open()


class SettingsText:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def open(self):
        SavesSettings().save_data_game_status('SettingsText')
        self.__view.settings_text()

    def check_press_mouse(self):
        x, y = pygame.mouse.get_pos()

        for btn in DataSettingsText().buttons():
            if btn.get_info_rect_button().collidepoint(x, y):
                if btn.get_info_button()[-1] == 'small_text':
                    PressButton.press_wood_button()
                    SavesSettings().save_text_size('small_text')
                if btn.get_info_button()[-1] == 'medium_text':
                    PressButton.press_wood_button()
                    SavesSettings().save_text_size('medium_text')
                if btn.get_info_button()[-1] == 'big_text':
                    PressButton.press_wood_button()
                    SavesSettings().save_text_size('big_text')
                if btn.get_info_button()[-1] == 'back':
                    PressButton.press_wood_button()
                    Settings(self.__view, self.__model).open()


class Settings:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__menu = SavesGameAndMode().get_menu_mod()

    def open(self):
        SavesSettings().save_data_game_status('Settings')
        self.__view.settings()

    def check_press_mouse(self):
        x, y = pygame.mouse.get_pos()
        for btn in DataSettings().buttons():
            if btn.get_info_rect_button().collidepoint(x, y):
                if btn.get_info_button()[-1] == 'audio':
                    PressButton.press_wood_button()
                    SettingsAudio(self.__view, self.__model).open()
                elif btn.get_info_button()[-1] == 'video':
                    PressButton.press_wood_button()
                    SettingsVideo(self.__view, self.__model).open()
                elif btn.get_info_button()[-1] == 'text':
                    PressButton.press_wood_button()
                    SettingsText(self.__view, self.__model).open()
                elif btn.get_info_button()[-1] == 'back':
                    PressButton.press_wood_button()
                    if self.__menu == 'main':
                        MainMenu(self.__view, self.__model).open()
                    else:
                        MiniMenu(self.__view, self.__model).open()


class MainMenu:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def open(self):
        SavesSettings().save_data_game_status('MainMenu')
        SavesGameAndMode().save_menu_mod('main')
        self.__view.main_menu()

    @staticmethod
    def preparation_a_new_game():
        SavesGameAndMode().save_the_presence_of_old_company(True)
        SavesGameAndMode().save_turn('user')
        participants = [SavesDeckAndCardsEnemy(), SavesDeckAndCardsUser()]
        for participant in participants:
            participant.save_deck([])
            Deck(participant).filling_the_deck_before_starting()
            participant.save_cards([0, 0, 0, 0, 0, 0])
            participant.save_unoccupied_positions([5, 4, 3, 2, 1, 0])
            participant.save_denominations_cards_on_hand([0] * 6)
            participant.save_denominations_segment_tree(SegmentTree.make_tree(SegmentTree.prepare_tree(6)))
            participant.save_allowed_card_draw(8)
            participant.save_count_cards(0)
            module_stats = participant.get_stats()
            module_stats.save_health(100)
            module_stats.save_armor(20)
            module_stats.save_mana(50)
        # sample_tree_enemy = [['None', 0], ['berserk', 25], ['cunning', 20], ['berserk', 25], ['None', 0],
        #                      ['cunning', 20], ['berserk', 25], ['prophet', 15], ['None', 0], ['None', 0],
        #                      ['stick', 15], ['cunning', 20], ['berserk', 25], ['stone', 10], ['prophet', 15],
        #                      ['cry', 10]]
        #
        # SavesDeckAndCardsEnemy().save_cards(CardsOnHand.get_sample())
        # SavesDeckAndCardsEnemy().save_denominations_segment_tree(sample_tree_enemy)

    def check_press_mouse(self):
        x, y = pygame.mouse.get_pos()
        for btn in DataMainMenu().buttons():
            if btn.get_info_rect_button().collidepoint(x, y):
                if btn.get_info_button()[-1] == 'new_game':
                    PressButton.press_wood_button()
                    self.preparation_a_new_game()
                    ChildHood(self.__view, self.__model).open()
                elif btn.get_info_button()[-1] == 'continue_game':
                    PressButton.press_wood_button()
                    if SavesGameAndMode().get_the_presence_of_old_company():
                        ChildHood(self.__view, self.__model).open()
                elif btn.get_info_button()[-1] == 'settings':
                    PressButton.press_wood_button()
                    Settings(self.__view, self.__model).open()
                elif btn.get_info_button()[-1] == 'quit':
                    self.__model.quit_game()


class MiniMenu:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def open(self):
        SavesSettings().save_data_game_status('IsPlaying')
        SavesGameAndMode().save_menu_mod('mini')
        self.__view.childhood_level(menu=True)

    def check_press_mouse(self):
        x, y = pygame.mouse.get_pos()
        for btn in DataMiniMenu().buttons():
            if btn.get_info_rect_button().collidepoint(x, y):
                if btn.get_info_button()[-1] == 'continue_playing':
                    PressButton.press_wood_button()
                    SavesGameAndMode().save_menu_mod('main')
                    ChildHood(self.__view, self.__model).open()
                elif btn.get_info_button()[-1] == 'settings':
                    PressButton.press_wood_button()
                    Settings(self.__view, self.__model).open()
                elif btn.get_info_button()[-1] == 'main_menu':
                    MainMenu(self.__view, self.__model).open()

        for btn in DataChildHoodInterface().buttons():
            if btn.get_info_rect_button().collidepoint(x, y):
                if btn.get_info_button()[-1] == 'playing_main_menu':
                    PressButton.press_wood_button()
                    SavesGameAndMode().save_menu_mod('main')
                    ChildHood(self.__view, self.__model).open()


class ChildHood:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.__menu = SavesGameAndMode().get_menu_mod()
        self.__opponent = ModulesOpponents.get_module_opponent()

    def open(self):
        SavesSettings().save_data_game_status('IsPlaying')
        if self.__menu == 'mini':
            self.__view.childhood_level(True)
        else:
            self.__view.childhood_level()

    def check_press_button(self, x: int, y: int, click_was: bool):
        for btn in DataChildHoodInterface().buttons():
            if btn.get_info_rect_button().collidepoint(x, y):
                click_was = True
                if btn.get_info_button()[-1] == 'mini_menu':
                    PressButton.press_wood_button()
                    MiniMenu(self.__view, self.__model).open()
                if btn.get_info_button()[-1] == 'get_card':
                    PressButton.press_wood_button()
                    if SavesGameAndMode().get_turn() == 'user':
                        LogicCardField(SavesDeckAndCardsUser(), SavesDeckAndCardsEnemy).get_one_card()
                if btn.get_info_button()[-1] == 'end_turn':
                    PressButton.press_wood_button()
                    SavesStatsEnemy().save_mana(50)
                    SavesGameAndMode().save_turn('enemy')
                    SavesDeckAndCardsEnemy().save_allowed_card_draw(6)
                    EnemyMove.make_damage()

        return click_was

    @staticmethod
    def check_press_card(x: int, y: int):
        number_user_card = -1
        click_on_card = False
        # number_chosen_card = SavesDeckAndCardsUser().get_chosen_card()
        for card in DataChildhoodUserCards().cards_user():
            number_user_card += 1
            if type(card) != int:
                method_card = card[0]
                if method_card.get_info_rect_card(number_user_card).collidepoint(x, y):
                    PressButton.press_wood_button()
                    number_chosen_card = number_user_card
                    SavesDeckAndCardsUser().save_chosen_card(number_chosen_card)
                    click_on_card = True
                    break
        return click_on_card

    @staticmethod
    def check_press_on_enemy(x: int, y: int):
        number_chosen_card = SavesDeckAndCardsUser().get_chosen_card()
        if type(number_chosen_card) == int:
            for enemy in DataChildhoodEnemy().enemy():
                if enemy.get_info_rect_enemy().collidepoint(x, y):
                    chosen_card = DataChildhoodUserCards.cards_user()[number_chosen_card]
                    if type(chosen_card) != int:
                        mana_chosen_card = chosen_card[1]
                        if SavesStatsUser().get_mana() >= mana_chosen_card:
                            chosen_card = number_chosen_card
                            cards_on_hand = CardsOnHand(SavesDeckAndCardsUser(), SavesDeckAndCardsEnemy)
                            cards_on_hand.use_ability_card_from_cards(chosen_card)
                            PressButton.press_wood_button()
                            if cards_on_hand.check_to_remove_chosen_card():
                                cards_on_hand.remove_one_card_in_cards(number_chosen_card)
                            break

    def check_press_mouse(self):
        click_on_card = False
        click_on_button = False
        if self.__menu == 'mini':
            MiniMenu(self.__view, self.__model).check_press_mouse()
        else:
            x, y = pygame.mouse.get_pos()
            click_on_button = self.check_press_button(x, y, click_on_button)
            if not click_on_button:
                click_on_card = self.check_press_card(x, y)
            if not click_on_button and not click_on_card:
                self.check_press_on_enemy(x, y)
        if not click_on_card:
            SavesDeckAndCardsUser().save_chosen_card()

