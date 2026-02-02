from data_base import SavesGameAndMode, SavesDeckAndCardsUser, SavesDeckAndCardsEnemy, SavesStatsUser, SavesStatsEnemy
from data_childhood import *
# from data_mini_menu import DataMiniMenu
from game_interface import LogicCardField
# from segment_tree import SegmentTree
from deck_and_cards_childhood import CardsOnHand
import pygame

pygame.init()


class EnemyMove:

    @staticmethod
    def take_card():
        number_of_cards_allowed = SavesDeckAndCardsEnemy().get_allowed_card_draw()
        count_cards_on_hand = SavesDeckAndCardsEnemy().get_count_cards()
        while number_of_cards_allowed != 0 and count_cards_on_hand != 6:
            LogicCardField(SavesDeckAndCardsEnemy(), SavesDeckAndCardsUser()).get_one_card()
            number_of_cards_allowed -= 1

    @staticmethod
    def make_damage():
        EnemyMove.take_card()
        number_enemy_card = -1
        cards = DataChildhoodEnemy().cards_enemy()
        # enemy_mana = SavesStatsEnemy().get_mana()
        for card in cards:
            number_enemy_card += 1
            if type(card) != int:
                # method_card = card[0]
                number_chosen_card = number_enemy_card
                chosen_card = cards[number_chosen_card]
                mana_chosen_card = chosen_card[1]
                if SavesStatsEnemy().get_mana() >= mana_chosen_card:
                    if SavesDeckAndCardsUser().get_count_cards() == 0 and chosen_card[0] == 'prophet':
                        pass
                    else:
                        SavesDeckAndCardsEnemy().save_chosen_card(number_chosen_card)
                        cards_on_hand = CardsOnHand(SavesDeckAndCardsEnemy(), SavesDeckAndCardsUser)
                        cards_on_hand.use_ability_card_from_cards(number_chosen_card)
                        if cards_on_hand.check_to_remove_chosen_card():
                            cards_on_hand.remove_one_card_in_cards(number_chosen_card)
                else:
                    SavesGameAndMode().save_turn('user')
                    SavesDeckAndCardsUser().save_allowed_card_draw(4)
                    SavesStatsUser().save_mana(50)
                    break
