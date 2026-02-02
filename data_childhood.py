from process_explorer import StandardFunctionality
from Cards import Stick
from data_base import SavesSettings, SavesDeckAndCardsUser, SavesDeckAndCardsEnemy, SavesStatsUser, SavesStatsEnemy
from button import Button
from game_interface import Stats
from deck_and_cards_childhood import CardsOnHand
from Enemies import Enemy


class DataChildHoodInterface:
    def __init__(self):
        self.__background = f'images/{SavesSettings().get_screen_status()[-1]}/childhood.jpg'
        self.__button_img = 'images/Button.jpg'
        self.__heart_img = 'images/heart.png'
        self.__armor_img = 'images/armor.png'
        self.__mana_img = 'images/mana.png'
        self._width_display, self._height_display = StandardFunctionality.window_size()

    def position_in_the_center(self, width: int):
        return self._width_display // 2 - width // 2

    def get_background_img(self):
        return self.__background

    def stats(self):
        WIDTH_HEART, HEIGHT_HEART = self._width_display // 16, self._height_display // 10
        size_heart = (WIDTH_HEART, HEIGHT_HEART)

        position_heart_user = (self._width_display / 11, self._height_display - self._height_display // 6)
        position_heart_enemy = (self._width_display / 7, self._height_display // 15)
        position_armor_user = (self._width_display * (9 / 11), self._height_display - self._height_display // 6)
        position_armor_enemy = (self._width_display * (5.3 / 7), self._height_display // 15)
        position_mana_user = (self._width_display * (9.5 / 11), self._height_display * (1.3 / 2))
        position_mana_enemy = (self._width_display * (9.5 / 11), self._height_display * (0.6 / 2))

        user_heart = Stats(position_heart_user, size_heart, text=str(SavesStatsUser().get_health()),
                           name='user_heart', img_path=self.__heart_img)

        enemy_heart = Stats(position_heart_enemy, size_heart, text=str(SavesStatsEnemy().get_health()),
                            name='enemy_heart', img_path=self.__heart_img)

        user_armor = Stats(position_armor_user, size_heart, text=str(SavesStatsUser().get_armor()),
                           name='user_armor', img_path=self.__armor_img)

        enemy_armor = Stats(position_armor_enemy, size_heart, text=str(SavesStatsEnemy().get_armor()),
                            name='enemy_armor', img_path=self.__armor_img)

        user_mana = Stats(position_mana_user, size_heart, text=str(SavesStatsUser().get_mana()), name='user_mana',
                          img_path=self.__mana_img)

        enemy_mana = Stats(position_mana_enemy, size_heart, text=str(SavesStatsEnemy().get_mana()), name='enemy_mana',
                           img_path=self.__mana_img)

        stats = [user_heart, enemy_heart, user_armor, enemy_armor, user_mana, enemy_mana]
        return stats

    def buttons(self):
        WIDTH_BUTTON_MINI_MENU = self._height_display * 0.09
        HEIGHT_BUTTON_MINI_MENU = self._height_display * 0.09
        size_mini_menu = (WIDTH_BUTTON_MINI_MENU, HEIGHT_BUTTON_MINI_MENU)

        WIDTH_BUTTON = self._width_display // 11
        HEIGHT_BUTTON = self._height_display // 15
        size_button = (WIDTH_BUTTON, HEIGHT_BUTTON)

        position_mini_menu = (self._width_display // 20 - WIDTH_BUTTON_MINI_MENU // 2, self._height_display // 20)

        position_get_card = (self._width_display - WIDTH_BUTTON * 1.1, self._height_display * (1.1 / 2))

        position_end_turn = (self._width_display - WIDTH_BUTTON * 1.1, self._height_display * (0.9 / 2))

        mini_menu = Button(position_mini_menu, size_mini_menu, text='||', name='mini_menu', img_path=self.__button_img)

        get_card = Button(position_get_card, size_button, text='Get card', name='get_card',
                          img_path=self.__button_img)

        end_turn = Button(position_end_turn, size_button, text='End turn', name='end_turn',
                          img_path=self.__button_img)
        childhood_buttons = [mini_menu, get_card, end_turn]
        return childhood_buttons


class DataChildhoodUserCards:
    @staticmethod
    def cards_user():
        childhood_cards_user = CardsOnHand(SavesDeckAndCardsUser(), SavesDeckAndCardsEnemy()).get_cards()
        return childhood_cards_user


class DataChildhoodEnemy:
    def __init__(self):
        self.__img_enemy = 'images/enemy.png'

    @staticmethod
    def cards_enemy():
        childhood_cards_enemy = CardsOnHand(SavesDeckAndCardsEnemy(), SavesDeckAndCardsUser()).get_cards()
        return childhood_cards_enemy

    def enemy(self):
        childhood_enemy = [Enemy(self.__img_enemy)]
        return childhood_enemy
