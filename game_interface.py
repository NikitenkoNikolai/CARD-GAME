from process_explorer import StandardFunctionality
from color import Colors
from data_base import SavesSettings, SavesDeckAndCardsUser, SavesDeckAndCardsEnemy
import pygame
from deck_and_cards_childhood import CardsOnHand


class Stats:
    def __init__(self, position, size, text, name, img_path=None):
        self.__pos_x, self.__pos_y = position
        self.__width, self.__height = size
        self.__text = text
        self.__name = name
        self.__img_path = img_path

    def get_info_status_screen(self):
        if not self.__img_path:
            img = None
            return img
        img = pygame.image.load(self.__img_path)
        img = pygame.transform.scale(img, (self.__width, self.__height))
        return img

    def draw(self, display_window):
        img = self.get_info_status_screen()
        if img:
            rect = img.get_rect(topleft=(self.__pos_x, self.__pos_y))
            current_img = img
            display_window.blit(current_img, rect.topleft)
        else:
            red = Colors.red()
            pygame.draw.rect(display_window, red, (self.__pos_x, self.__pos_y, self.__width, self.__height))

        white = Colors().white()
        font = pygame.font.Font(None, SavesSettings().get_text_size())
        text_surface = font.render(self.__text, True, white)
        center = (self.__pos_x + self.__width * 1.5, self.__pos_y + self.__height // 2)
        text_rect = text_surface.get_rect(center=center)
        display_window.blit(text_surface, text_rect)


class CardField:

    def __init__(self):
        self.__width_display, self.__height_display = StandardFunctionality.window_size()
        self.__left_border = self.__width_display // 4
        self.__right_border = self.__width_display * 2.5

    def get_pos_card_field(self):
        return [self.__left_border, self.__right_border]


class LogicCardField:
    def __init__(self, opponent: SavesDeckAndCardsUser or SavesDeckAndCardsEnemy,
                 victim: SavesDeckAndCardsEnemy or SavesDeckAndCardsUser):
        self.__victim = victim
        self.__opponent = opponent
        self.__left_border, self.__right_border = CardField().get_pos_card_field()
        self.__count_cards = self.__opponent.get_count_cards()

    def get_one_card(self):
        # user_deck = self.__opponent.get_deck()
        count_user_cards = self.__opponent.get_count_cards()

        possible_count_cards = self.__opponent.get_allowed_card_draw()
        if count_user_cards < 6 and possible_count_cards > 0:
            self.__opponent.save_allowed_card_draw(possible_count_cards - 1)
            return CardsOnHand(self.__opponent, self.__victim).add_one_card_in_cards()

    @staticmethod
    def distribute_card_positions(width_card, number_card):
        left_border = StandardFunctionality.window_size()[0] // 4
        SPACE_BETWEEN_CARDS = width_card // 8
        if number_card == 0:
            return left_border
        else:
            return left_border + number_card * width_card + SPACE_BETWEEN_CARDS * number_card

    @staticmethod
    def check_selected_card():
        number_card = SavesDeckAndCardsUser().get_chosen_card()
        if type(number_card) == int:
            return number_card
