import sqlite3
import pyautogui
import ast


class Saves:
    def __init__(self):
        self.file_settings = sqlite3.connect('data_base.db')
        self.cursor = self.file_settings.cursor()

    # def __del__(self):
    #     self.file_settings.close()


class SavesSettings(Saves):

    def get_screen_status(self):
        columns = {'full_screen': 5, 'window_screen': 6, 'full_screen_now': 7, 'window_screen_now': 8}
        values = self.get_data_settings()
        if values[columns['full_screen_now']]:
            width, height = self.get_size_screen()
            return [width, height, 'full_screen']
        else:
            return [1400, 768, 'window_screen']

    @staticmethod
    def get_size_screen():
        return pyautogui.size()

    def get_text_size(self):
        width, height = self.get_size_screen()
        columns = {'small_text': [9, width // 40], 'medium_text': [10, width // 30], 'big_text': [11, width // 20]}
        values = self.get_data_settings()
        for size_text in columns:
            if values[columns[size_text][0]] == 1:
                return columns[size_text][1]

    def save_data_settings(self, key: str, value):
        self.cursor.execute(f'''UPDATE data_settings SET {key} = {value}''')
        self.file_settings.commit()

    def get_data_settings(self):
        return tuple(*self.cursor.execute('''SELECT * FROM data_settings'''))

    def save_data_game_status(self, value: str):
        statuses = {'MainMenu': 0, 'Settings': 1, 'SettingsText': 2, 'SettingsVideo': 3, 'SettingsAudio': 4,
                    'IsPlaying': 5}
        self.cursor.execute(f"UPDATE data_game_status SET status = {statuses[value]}")
        self.file_settings.commit()

    def get_data_game_status(self):
        statuses = {0: 'MainMenu', 1: 'Settings', 2: 'SettingsText', 3: 'SettingsVideo', 4: 'SettingsAudio',
                    5: 'IsPlaying'}
        return statuses[tuple(*self.cursor.execute('''SELECT * FROM data_game_status'''))[0]]

    @staticmethod
    def save_settings_info_video():
        columns = {'full_screen_box': 3, 'window_screen_box': 4, 'full_screen': 5, 'window_screen': 6}
        values = SavesSettings().get_data_settings()
        SavesSettings().save_data_settings('full_screen', values[columns['full_screen_box']])
        SavesSettings().save_data_settings('window_screen', values[columns['window_screen_box']])

    @staticmethod
    def save_status_screen(screen_mod: str):
        if screen_mod == 'full_screen_box':
            SavesSettings().save_data_settings('full_screen_box', True)
            SavesSettings().save_data_settings('window_screen_box', False)
        else:
            SavesSettings().save_data_settings('full_screen_box', False)
            SavesSettings().save_data_settings('window_screen_box', True)

    @staticmethod
    def save_text_size(selected_size_text: str):
        if selected_size_text:
            if selected_size_text == 'small_text':
                SavesSettings().save_data_settings('small_text', 1)
                SavesSettings().save_data_settings('medium_text', 0)
                SavesSettings().save_data_settings('big_text', 0)
            if selected_size_text == 'medium_text':
                SavesSettings().save_data_settings('small_text', 0)
                SavesSettings().save_data_settings('medium_text', 1)
                SavesSettings().save_data_settings('big_text', 0)
            if selected_size_text == 'big_text':
                SavesSettings().save_data_settings('small_text', 0)
                SavesSettings().save_data_settings('medium_text', 0)
                SavesSettings().save_data_settings('big_text', 1)


class SavesGameAndMode(Saves):
    def save_menu_mod(self, value: str):
        menu = {'main': 0, 'mini': 1}
        self.cursor.execute(f"UPDATE data_game_status SET menu = {menu[value]}")
        self.file_settings.commit()

    def get_menu_mod(self):
        menu = {0: 'main', 1: 'mini'}
        return menu[tuple(*self.cursor.execute('''SELECT * FROM data_game_status'''))[1]]

    def save_the_presence_of_old_company(self, answer: bool):
        self.cursor.execute(f"UPDATE data_card_board SET game_company = {answer}")
        self.file_settings.commit()

    def get_the_presence_of_old_company(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[9]
        return answer

    def save_turn(self, answer: str):
        turn = {'enemy': 0, 'user': 1}
        self.cursor.execute(f"UPDATE data_game_status SET user_turn = {turn[answer]}")
        self.file_settings.commit()

    def get_turn(self):
        turn = {0: 'enemy', 1: 'user'}
        answer = turn[tuple(*self.cursor.execute('''SELECT * FROM data_game_status'''))[2]]
        return answer


class SavesDeckAndCardsUser(Saves):
    @staticmethod
    def get_stats():
        return SavesStatsUser()

    def save_count_cards(self, value: int):
        self.cursor.execute(f"UPDATE data_card_board SET count_user_cards = {value}")
        self.file_settings.commit()

    def get_count_cards(self):
        return tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[0]

    def save_cards(self, cards: list):
        cards = f'"{str(cards)}"'
        self.cursor.execute(f"UPDATE data_card_board SET user_cards = {cards}")
        self.file_settings.commit()

    def get_cards(self):
        cards = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[1])
        return cards

    def save_deck(self, deck: list):
        deck = f'"{str(deck)}"'
        self.cursor.execute(f"UPDATE data_card_board SET user_deck = {deck}")
        self.file_settings.commit()

    def get_deck(self):
        deck = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[2])
        return deck

    def save_allowed_card_draw(self, count: int):
        self.cursor.execute(f"UPDATE data_card_board SET user_allowed_card_draws = {count}")
        self.file_settings.commit()

    def get_allowed_card_draw(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[3]
        return answer

    def save_chosen_card(self, number_card=None):
        if type(number_card) == int:
            self.cursor.execute(f"UPDATE data_card_board SET chosen_user_card = {number_card}")
        else:
            self.cursor.execute(f"UPDATE data_card_board SET chosen_user_card = 'None'")
        self.file_settings.commit()

    def get_chosen_card(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[4]
        return answer

    def save_unoccupied_positions(self, unoccupied_positions: list[int]):
        unoccupied_positions = f'"{str(unoccupied_positions)}"'
        self.cursor.execute(f"UPDATE data_card_board SET user_unoccupied_positions = {unoccupied_positions}")
        self.file_settings.commit()

    def get_unoccupied_positions(self):
        answer = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[10])
        return answer

    def save_denominations_cards_on_hand(self, denominations: list[int]):
        denominations = f'"{str(denominations)}"'
        self.cursor.execute(f"UPDATE data_denominations_cards_on_hand SET user_denominations = {denominations}")
        self.file_settings.commit()

    def get_denominations_cards_on_hand(self):
        answer = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_denominations_cards_on_hand'''))[0])
        return answer

    def save_denominations_segment_tree(self, denominations: list[int]):
        denominations = f'"{str(denominations)}"'
        self.cursor.execute(f"UPDATE data_denominations_cards_on_hand SET user_segment_tree = {denominations}")
        self.file_settings.commit()

    def get_denominations_segment_tree(self):
        answer = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_denominations_cards_on_hand'''))[2])
        return answer


class SavesDeckAndCardsEnemy(Saves):
    @staticmethod
    def get_stats():
        return SavesStatsEnemy()

    def save_count_cards(self, value: int):
        self.cursor.execute(f"UPDATE data_card_board SET count_enemy_cards = {value}")
        self.file_settings.commit()

    def get_count_cards(self):
        return tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[5]

    def save_cards(self, cards: list):
        cards = f'"{str(cards)}"'
        self.cursor.execute(f"UPDATE data_card_board SET enemy_cards = {cards}")
        self.file_settings.commit()

    def get_cards(self):
        cards = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[6])
        return cards

    def save_deck(self, deck: list):
        deck = f'"{str(deck)}"'
        self.cursor.execute(f"UPDATE data_card_board SET enemy_deck = {deck}")
        self.file_settings.commit()

    def get_deck(self):
        deck = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[7])
        return deck

    def save_allowed_card_draw(self, count: int):
        self.cursor.execute(f"UPDATE data_card_board SET enemy_allowed_card_draws = {count}")
        self.file_settings.commit()

    def get_allowed_card_draw(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[8]
        return answer

    def save_unoccupied_positions(self, unoccupied_positions: list[int]):
        unoccupied_positions = f'"{str(unoccupied_positions)}"'
        self.cursor.execute(f"UPDATE data_card_board SET enemy_unoccupied_positions = {unoccupied_positions}")
        self.file_settings.commit()

    def get_unoccupied_positions(self):
        answer = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[11])
        return answer

    def save_denominations_cards_on_hand(self, denominations: list[int]):
        denominations = f'"{str(denominations)}"'
        self.cursor.execute(f"UPDATE data_denominations_cards_on_hand SET enemy_denominations = {denominations}")
        self.file_settings.commit()

    def get_denominations_cards_on_hand(self):
        answer = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_denominations_cards_on_hand'''))[1])
        return answer

    def save_denominations_segment_tree(self, denominations: list[int]):
        denominations = f'"{str(denominations)}"'
        self.cursor.execute(f"UPDATE data_denominations_cards_on_hand SET enemy_segment_tree = {denominations}")
        self.file_settings.commit()

    def get_denominations_segment_tree(self):
        answer = ast.literal_eval(tuple(*self.cursor.execute('''SELECT * FROM data_denominations_cards_on_hand'''))[3])
        return answer

    def save_chosen_card(self, number_card=None):
        if type(number_card) == int:
            self.cursor.execute(f"UPDATE data_card_board SET enemy_chosen_card = {number_card}")
        else:
            self.cursor.execute(f"UPDATE data_card_board SET enemy_chosen_card = 'None'")
        self.file_settings.commit()

    def get_chosen_card(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_card_board'''))[12]
        return answer


class SavesStatsUser(SavesDeckAndCardsUser):
    def save_health(self, count: int):
        self.cursor.execute(f"UPDATE data_opponents_characteristics SET user_health = {count}")
        self.file_settings.commit()

    def get_health(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_opponents_characteristics'''))[0]
        return answer

    def save_armor(self, count: int):
        self.cursor.execute(f"UPDATE data_opponents_characteristics SET user_armor = {count}")
        self.file_settings.commit()

    def get_armor(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_opponents_characteristics'''))[2]
        return answer

    def save_mana(self, count: int):
        self.cursor.execute(f"UPDATE data_opponents_characteristics SET user_mana = {count}")
        self.file_settings.commit()

    def get_mana(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_opponents_characteristics'''))[4]
        return answer


class SavesStatsEnemy(SavesDeckAndCardsEnemy):
    def save_health(self, count: int):
        self.cursor.execute(f"UPDATE data_opponents_characteristics SET enemy_health = {count}")
        self.file_settings.commit()

    def get_health(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_opponents_characteristics'''))[1]
        return answer

    def save_armor(self, count: int):
        self.cursor.execute(f"UPDATE data_opponents_characteristics SET enemy_armor = {count}")
        self.file_settings.commit()

    def get_armor(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_opponents_characteristics'''))[3]
        return answer

    def save_mana(self, count: int):
        self.cursor.execute(f"UPDATE data_opponents_characteristics SET enemy_mana = {count}")
        self.file_settings.commit()

    def get_mana(self):
        answer = tuple(*self.cursor.execute('''SELECT * FROM data_opponents_characteristics'''))[5]
        return answer
