import Cards
from data_base import SavesDeckAndCardsUser, SavesDeckAndCardsEnemy
from segment_tree import SegmentTree
import random


class Deck:
    def __init__(self, opponent: SavesDeckAndCardsUser or SavesDeckAndCardsEnemy):
        self.__set_cards = self.get_set_cards()
        self.__opponent = opponent
        self.__deck = self.__opponent.get_deck()

    @staticmethod
    def get_set_cards():
        return {'stick': [Cards.Stick(), Cards.Stick().get_consumption()],
                'stone': [Cards.Stone(), Cards.Stone().get_consumption()],
                'cuteness': [Cards.Cuteness(), Cards.Cuteness().get_consumption()],
                'cunning': [Cards.Cunning(), Cards.Cunning().get_consumption()],
                'cry': [Cards.Cry(), Cards.Cry().get_consumption()],
                'berserk': [Cards.Berserk(), Cards.Berserk().get_consumption()],
                'prophet': [Cards.Prophet(), Cards.Prophet().get_consumption()]}

    def include_cards_in_the_deck(self, count: int, name_card: str, mana: int):
        for i in range(count):
            self.__deck.append([name_card, mana])
            self.__opponent.save_deck(self.__deck)

    def filling_the_deck_before_starting(self):
        self.include_cards_in_the_deck(2, 'cuteness', self.__set_cards['cuteness'][1])
        self.include_cards_in_the_deck(4, 'stone', self.__set_cards['stone'][1])  # 4
        self.include_cards_in_the_deck(2, 'berserk', self.__set_cards['berserk'][1])  # 2
        self.include_cards_in_the_deck(2, 'stick', self.__set_cards['stick'][1])
        self.include_cards_in_the_deck(1, 'cunning', self.__set_cards['cunning'][1])
        self.include_cards_in_the_deck(4, 'cry', self.__set_cards['cry'][1])
        self.include_cards_in_the_deck(2, 'prophet', self.__set_cards['prophet'][1])
        random.shuffle(self.__deck)
        self.__opponent.save_deck(self.__deck)

    def get_deck(self):
        return self.__deck


class CardsOnHand:
    def __init__(self, opponent: SavesDeckAndCardsUser or SavesDeckAndCardsEnemy,
                 victim: SavesDeckAndCardsEnemy or SavesDeckAndCardsUser):
        self.__set_cards = Deck.get_set_cards()
        self.__opponent = opponent
        self.__victim = victim
        self.__deck = self.__opponent.get_deck()
        self.__cards = self.__opponent.get_cards()
        self.__remove_card = True

    @staticmethod
    def get_sample():
        return [['stick', 15], ['cunning', 20], ['berserk', 25], ['stone', 10], ['prophet', 15], ['cry', 10]]

    def check_to_remove_chosen_card(self):
        return self.__remove_card

    def translate_card_data(self):
        for card in range(len(self.__cards)):
            if type(self.__cards[card]) == int:
                pass
            elif self.__cards[card][0] == 'stone':
                self.__cards[card][0] = self.__set_cards['stone'][0]
            elif self.__cards[card][0] == 'stick':
                self.__cards[card][0] = self.__set_cards['stick'][0]
            elif self.__cards[card][0] == 'cunning':
                self.__cards[card][0] = self.__set_cards['cunning'][0]
            elif self.__cards[card][0] == 'cuteness':
                self.__cards[card][0] = self.__set_cards['cuteness'][0]
            elif self.__cards[card][0] == 'cry':
                self.__cards[card][0] = self.__set_cards['cry'][0]
            elif self.__cards[card][0] == 'berserk':
                self.__cards[card][0] = self.__set_cards['berserk'][0]
            elif self.__cards[card][0] == 'prophet':
                self.__cards[card][0] = self.__set_cards['prophet'][0]

    def get_cards(self) -> list:
        self.translate_card_data()
        return self.__cards

    def add_one_card_in_cards(self):
        self.__opponent.save_count_cards(self.__opponent.get_count_cards() + 1)
        unoccupied_positions = self.__opponent.get_unoccupied_positions()
        index = unoccupied_positions[-1]
        card = self.__deck[0]
        self.__cards[index] = card
        self.__deck = self.__deck[1:]
        self.__opponent.save_deck(self.__deck)
        self.__opponent.save_cards(self.__cards)
        self.create_denominations_opponent(self.__cards, index)

        tree = self.__opponent.get_denominations_segment_tree()
        index = SegmentTree.translate_index(tree, self.__cards, index)
        SegmentTree.update(tree, self.__cards, index, card)
        self.__opponent.save_denominations_segment_tree(tree)
        self.__opponent.save_unoccupied_positions(unoccupied_positions[:-1])

    def create_denominations_opponent(self, opponent_cards: list[[str, int]], number_card_created: int, operation=True):
        denominations = self.__opponent.get_denominations_cards_on_hand()
        value_card = opponent_cards[number_card_created][1]
        right_border = len(denominations) - 1
        index = number_card_created
        while 0 <= number_card_created <= right_border:
            if not operation:
                denominations[number_card_created] -= value_card
            else:
                denominations[number_card_created] += value_card
            index |= number_card_created + 1
            number_card_created = index
        self.__opponent.save_denominations_cards_on_hand(denominations)

    def use_ability_card_from_cards(self, number_card: int):
        key_card = self.__cards[number_card][0]
        card = self.__set_cards[key_card][0]
        old_card = key_card
        card.use_ability(self.__opponent.get_stats(), self.__victim.get_stats())
        self.__cards[number_card][0] = card.get_name()
        self.__opponent.save_cards(self.__cards)
        if old_card == self.__cards[number_card][0]:
            self.__remove_card = True
        else:
            self.__remove_card = False

    def remove_one_card_in_cards(self, number_card: int):
        count_user_cards = self.__opponent.get_count_cards()
        number_chosen_card = self.__opponent.get_chosen_card()
        name_chosen_card = self.__opponent.get_cards()[number_chosen_card][0]
        clear_card = ['None', 0]
        unoccupied_positions = self.__opponent.get_unoccupied_positions()
        unoccupied_positions.append(number_chosen_card)
        self.__opponent.save_unoccupied_positions(unoccupied_positions)
        tree = self.__opponent.get_denominations_segment_tree()
        index = SegmentTree.translate_index(tree, self.__cards, number_card)
        SegmentTree.update(tree, self.__cards, index, clear_card)
        self.__opponent.save_denominations_segment_tree(tree)
        self.__deck.append(self.__cards[number_card])
        self.__cards[number_card] = 0
        self.__opponent.save_count_cards(count_user_cards - 1)
        Deck(self.__opponent).include_cards_in_the_deck(1, name_chosen_card, self.__set_cards[name_chosen_card][1])

        self.create_denominations_opponent(self.__opponent.get_cards(), number_chosen_card, False)

        self.__opponent.save_deck(self.__deck)
        self.__opponent.save_cards(self.__cards)
