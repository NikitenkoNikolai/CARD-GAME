from process_explorer import StandardFunctionality
from color import Colors
import pygame
from data_base import SavesStatsUser, SavesStatsEnemy
from game_interface import LogicCardField
from segment_tree import SegmentTree


class Card:
    def __init__(self):
        self._width_display, self._height_display = StandardFunctionality.window_size()
        self._width_card, self._height_card = self._width_display // 13, self._height_display // 4.2
        self._img = None
        self._img_path = None

    def get_info_rect_card(self, number_card: int):
        pos_y = self.take_pos_y_card(number_card)
        pos_x = self.take_pos_x_card(number_card)
        return pygame.Rect(pos_x, pos_y, self._width_card, self._height_card)

    def get_info_size_card(self):
        return [self._width_card, self._height_card]

    def take_pos_x_card(self, number_card: int):
        return LogicCardField.distribute_card_positions(self._width_card, number_card)

    def take_pos_y_card(self, number_card: int):
        selected_card = LogicCardField.check_selected_card()
        if type(selected_card) == int and number_card == selected_card:
            return self._height_display - self._height_card - self._height_card // 3
        else:
            return self._height_display - self._height_card - self._height_card // 5

    def get_info_status_screen(self):
        if not self._img_path:
            self._img = None
            return self._img
        self._img = pygame.image.load(self._img_path)
        self._img = pygame.transform.scale(self._img, (self._width_card, self._height_card))
        return self._img

    @staticmethod
    def distribute_damage(target: SavesStatsUser or SavesStatsEnemy, damage: int, health: int,
                          armor: int):
        remainder_armor = armor - damage
        if remainder_armor >= 0:
            target.save_armor(remainder_armor)
        else:
            target.save_armor(0)
            now_health = health + remainder_armor if health + remainder_armor > 0 else 0
            target.save_health(now_health)

    def draw(self, display_window, number_card):
        pos_y = self.take_pos_y_card(number_card)
        pos_x = self.take_pos_x_card(number_card)
        self._img = self.get_info_status_screen()
        white = Colors.white()
        black = Colors.black()
        if self._img:
            rect = self._img.get_rect(topleft=(pos_x, pos_y))
            current_img = self._img
            display_window.blit(current_img, rect.topleft)
        else:
            pygame.draw.rect(display_window, white, (pos_x, pos_y, self._width_card, self._height_card))


class Stick(Card):
    def __init__(self):
        super().__init__()
        self.__name = 'stick'
        self._img_path = 'images/Cards/Stick.png'
        if self._img_path:
            self._img = pygame.image.load(self._img_path)
            self._img = pygame.transform.scale(self._img, (self._width_card, self._height_card))
        else:
            self._img = None

    def use_ability(self, opponent: SavesStatsUser or SavesStatsEnemy, victim: SavesStatsUser or SavesStatsEnemy):

        opponent.save_mana(opponent.get_mana() - Stick.get_consumption())
        health = victim.get_health()
        armor = victim.get_armor()
        damage = 15
        Card().distribute_damage(victim, damage, health, armor)

    def get_name(self) -> str:
        return self.__name

    @staticmethod
    def get_consumption():
        return 15


class Stone(Card):
    def __init__(self):
        super().__init__()
        self.__name = 'stone'
        self._img_path = 'images/Cards/Stone.png'
        if self._img_path:
            self._img = pygame.image.load(self._img_path)
            self._img = pygame.transform.scale(self._img, (self._width_card, self._height_card))
        else:
            self._img = None

    def use_ability(self, opponent: SavesStatsUser or SavesStatsEnemy, victim: SavesStatsUser or SavesStatsEnemy):
        opponent.save_mana(opponent.get_mana() - Stone.get_consumption())
        health = victim.get_health()
        armor = victim.get_armor()
        damage = 10
        Card().distribute_damage(victim, damage, health, armor)

    def get_name(self) -> str:
        return self.__name

    @staticmethod
    def get_consumption():
        return 10


class Cry(Card):
    def __init__(self):
        super().__init__()
        self.__name = 'cry'
        self._img_path = 'images/Cards/Cry.png'
        if self._img_path:
            self._img = pygame.image.load(self._img_path)
            self._img = pygame.transform.scale(self._img, (self._width_card, self._height_card))
        else:
            self._img = None

    def use_ability(self, opponent: SavesStatsUser or SavesStatsEnemy, victim: SavesStatsUser or SavesStatsEnemy):
        opponent.save_mana(opponent.get_mana() - Cry.get_consumption())
        armor = opponent.get_armor()
        buff = 15
        opponent.save_armor(armor + buff)

    def get_name(self) -> str:
        return self.__name

    @staticmethod
    def get_consumption():
        return 10


class Cunning(Card):
    def __init__(self):
        super().__init__()
        self.__name = 'cunning'
        self._img_path = 'images/Cards/Cunning.png'
        if self._img_path:
            self._img = pygame.image.load(self._img_path)
            self._img = pygame.transform.scale(self._img, (self._width_card, self._height_card))
        else:
            self._img = None

    def use_ability(self, opponent: SavesStatsUser or SavesStatsEnemy, victim: SavesStatsUser or SavesStatsEnemy):
        opponent.save_mana(opponent.get_mana() - Cunning.get_consumption())
        opponent_health = opponent.get_health()
        opponent_armor = opponent.get_armor()
        opponent.save_armor(opponent_health)
        victim.save_armor(opponent.get_armor() // 5)
        opponent.save_health(opponent_armor)

    def get_name(self) -> str:
        return self.__name

    @staticmethod
    def get_consumption():
        return 20


class Cuteness(Card):
    def __init__(self):
        super().__init__()
        self.__name = 'cuteness'
        self._img_path = 'images/Cards/Cuteness.png'
        if self._img_path:
            self._img = pygame.image.load(self._img_path)
            self._img = pygame.transform.scale(self._img, (self._width_card, self._height_card))
        else:
            self._img = None

    def use_ability(self, opponent: SavesStatsUser or SavesStatsEnemy, victim: SavesStatsUser or SavesStatsEnemy):
        opponent.save_mana(opponent.get_mana() - Cuteness.get_consumption())
        health = opponent.get_health()
        buff = 10
        opponent.save_health(health + buff)

    def get_name(self) -> str:
        return self.__name

    @staticmethod
    def get_consumption():
        return 10


class Berserk(Card):
    def __init__(self):
        super().__init__()
        self.__name = 'berserk'
        self._img_path = 'images/Cards/Berserk.png'
        if self._img_path:
            self._img = pygame.image.load(self._img_path)
            self._img = pygame.transform.scale(self._img, (self._width_card, self._height_card))
        else:
            self._img = None

    @staticmethod
    def take_sum_line_segment(index: int, denominations: list[int]):
        sum_line_segment = 0
        while 0 <= index:
            sum_line_segment += denominations[index]
            index &= index + 1
            index -= 1
        return sum_line_segment

    def use_ability(self, opponent: SavesStatsUser or SavesStatsEnemy, victim: SavesStatsUser or SavesStatsEnemy):
        opponent.save_mana(opponent.get_mana() - Berserk().get_consumption())
        max_cards_on_hand = 5
        number_chosen_card = opponent.get_chosen_card()
        denominations = opponent.get_denominations_cards_on_hand()
        opponent_health = opponent.get_health()
        opponent_armor = opponent.get_armor()
        victim_health = victim.get_health()
        victim_armor = victim.get_armor()

        small_pref = Berserk().take_sum_line_segment(number_chosen_card, denominations)
        right_border = number_chosen_card + 3 if number_chosen_card + 3 <= max_cards_on_hand else max_cards_on_hand
        big_pref = Berserk().take_sum_line_segment(right_border, denominations)
        difference = big_pref - small_pref

        damage = difference if difference >= 0 else 0
        Card().distribute_damage(victim, damage // 2, victim_health, victim_armor)
        Card().distribute_damage(opponent, damage // 3, opponent_health, opponent_armor)

    def get_name(self) -> str:
        return self.__name

    @staticmethod
    def get_consumption():
        return 25


class Prophet(Card):
    def __init__(self):
        self.__name = 'prophet'
        super().__init__()
        self._img_path = 'images/Cards/Prophet.png'
        if self._img_path:
            self._img = pygame.image.load(self._img_path)
            self._img = pygame.transform.scale(self._img, (self._width_card, self._height_card))
        else:
            self._img = None

    def use_ability(self, opponent: SavesStatsUser or SavesStatsEnemy, victim: SavesStatsUser or SavesStatsEnemy):
        opponent.save_mana(opponent.get_mana() - Prophet().get_consumption())
        new_name = SegmentTree.get_max(victim.get_denominations_segment_tree(), victim.get_cards())[0]
        if new_name == 'None':
            self.create_name('cry')
        else:
            self.create_name(new_name)

    def create_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    @staticmethod
    def get_consumption():
        return 15
