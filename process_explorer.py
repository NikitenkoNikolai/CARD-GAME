from data_base import SavesSettings


class StandardFunctionality:

    @staticmethod
    def window_size():
        width_display, height_display = SavesSettings().get_screen_status()[0], SavesSettings().get_screen_status()[1]
        return width_display, height_display

    @staticmethod
    def quit_game():
        columns = {'full_screen': 5, 'window_screen': 6, 'full_screen_now': 7, 'window_screen_now': 8}
        values = SavesSettings().get_data_settings()
        SavesSettings().save_data_settings('full_screen_now', values[columns['full_screen']])
        SavesSettings().save_data_settings('window_screen_now', values[columns['window_screen']])
        SavesSettings().save_data_game_status('MainMenu')
        exit(0)
