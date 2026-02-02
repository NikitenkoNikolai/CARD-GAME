from button import Button, Slider
from data_base import SavesSettings
from color import Colors
from process_explorer import StandardFunctionality


class InterfaceData:
    def __init__(self):
        self._background = f'images/{SavesSettings().get_screen_status()[-1]}/settings_background.png'
        self._button_img = 'images/Button.jpg'
        self._width_display, self._height_display = StandardFunctionality.window_size()
        self.__WIDTH_BUTTON_CONST = self._width_display // 7
        self.__HEIGHT_BUTTON_CONST = self._height_display // 15
        self.__size_button = (self.__WIDTH_BUTTON_CONST, self.__HEIGHT_BUTTON_CONST)

    def position_in_the_center(self, width: int):
        return self._width_display // 2 - width // 2

    def position_in_the_center_button(self):
        return self.position_in_the_center(self.get_size_button()[0])

    def arrange_evenly_vert(self, count_elem: int, elem_order: int):
        return self._height_display * elem_order / (count_elem + 1)

    def get_size_button(self):
        return self.__size_button

    def get_background_img(self):
        return self._background


class DataSettingsAudio(InterfaceData):
    def __init__(self):
        super().__init__()
        self.__point_img = 'images/sckroll_point.png'
        self.__bond_img = 'images/sckroll.png'
        self.__count_elem = 4
        self.__WIDTH_BOND = self._width_display // 2.5
        self.__HEIGHT_BOND = 25

    def get_size_bond(self):
        return [self.__WIDTH_BOND, self.__HEIGHT_BOND]

    def sliders(self):
        WIDTH_POINT = 60
        HEIGHT_POINT = 80
        position_in_the_center_bond = self.position_in_the_center(self.__WIDTH_BOND)

        position_all = (position_in_the_center_bond, self.arrange_evenly_vert(self.__count_elem, 1))
        position_music = (position_in_the_center_bond, self.arrange_evenly_vert(self.__count_elem, 2))
        position_effects = (position_in_the_center_bond, self.arrange_evenly_vert(self.__count_elem, 3))
        size_bond = (self.__WIDTH_BOND, self.__HEIGHT_BOND)
        size_point = (WIDTH_POINT, HEIGHT_POINT)

        description_text_all = 'Audio all'
        description_text_music = 'Audio music'
        description_text_effects = 'Audio effects'

        description_pos_all = position_all[0] + size_bond[0] // 2, position_all[1] - size_bond[1] * 2
        description_pos_music = position_music[0] + size_bond[0] // 2, position_music[1] - size_bond[
            1] * 2
        description_pos_effects = position_effects[0] + size_bond[0] // 2, position_effects[1] - size_bond[
            1] * 2

        __all = Slider(position_all, size_bond, size_point, 'audio_all', self.__point_img,
                       self.__bond_img,
                       description_text_all, description_pos_all)

        __music = Slider(position_music, size_bond, size_point, 'audio_music', self.__point_img,
                         self.__bond_img,
                         description_text_music, description_pos_music)

        __effects = Slider(position_effects, size_bond, size_point, 'audio_effects', self.__point_img,
                           self.__bond_img, description_text_effects, description_pos_effects)

        __audio_sliders = [__all, __music, __effects]
        return __audio_sliders

    def buttons(self):
        position_back = (self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 4))
        back_button = Button(position_back, self.get_size_button(), text='Back', name='back', img_path=self._button_img)
        audio_buttons = [back_button]
        return audio_buttons


class DataSettingsVideo(InterfaceData):
    def __init__(self):
        super().__init__()
        self.__select_box_on = 'images/select_box_on.jpg'
        self.__select_box_off = 'images/select_box_off.jpg'
        self.__count_elem = 4

    def select_box(self):
        SIDE_BOX = self._height_display // 25
        position_select_box_horizontally = self._width_display - self._width_display // 2.5

        position_full_screen = (
            position_select_box_horizontally, self.arrange_evenly_vert(self.__count_elem, 1))
        position_window_screen = (
            position_select_box_horizontally, self.arrange_evenly_vert(self.__count_elem, 2))
        size = (SIDE_BOX, SIDE_BOX)
        description_text_full = 'Full screen'
        description_pos_full = (position_full_screen[0] // 2, position_full_screen[1] + 12)
        description_text_window = 'Window screen'
        description_pos_window = (position_window_screen[0] // 2, position_window_screen[1] + 12)
        full_screen = Button(position_full_screen, size, name='full_screen_box', img_path=self.__select_box_off,
                             img_path_push=self.__select_box_on, description_text=description_text_full,
                             description_pos=description_pos_full)
        window_screen = Button(position_window_screen, size, name='window_screen_box', img_path=self.__select_box_off,
                               img_path_push=self.__select_box_on, description_text=description_text_window,
                               description_pos=description_pos_window)
        select_boxes = [full_screen, window_screen]
        return select_boxes

    def buttons(self):
        position_save = (self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 3))
        position_back = (self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 4))
        description_text_save = 'Screen settings will be applied after reboot'
        description_pos_save = (position_save[0] + self.get_size_button()[0] // 2, self._height_display * 2.5 / 5)

        save = Button(position_save, self.get_size_button(), text='Save', name='save', img_path=self._button_img,
                      description_text=description_text_save, description_text_size=30,
                      description_text_color=Colors.red(), description_pos=description_pos_save)

        back = Button(position_back, self.get_size_button(), text='Back', name='back', img_path=self._button_img)

        buttons = [save, back]
        return buttons


class DataSettingsText(InterfaceData):
    def __init__(self):
        super().__init__()

    def buttons(self):
        position_small = (self._width_display // 2 - self.get_size_button()[0] * 2, self._height_display * 1.5 / 5)
        position_medium = (self.position_in_the_center_button(), self._height_display * 1.5 / 5)
        position_big = (self._width_display // 2 + self.get_size_button()[0], self._height_display * 1.5 / 5)
        position_back = (self._width_display // 2 - self.get_size_button()[0] // 2, self._height_display * 4 / 5)

        small = Button(position_small, self.get_size_button(), text='Small text', name='small_text',
                       img_path=self._button_img)

        medium = Button(position_medium, self.get_size_button(), text='Medium text', name='medium_text',
                        img_path=self._button_img)

        big = Button(position_big, self.get_size_button(), text='Big text', name='big_text',
                     img_path=self._button_img)

        back = Button(position_back, self.get_size_button(), text='Back', name='back', img_path=self._button_img)

        buttons = [small, medium, big, back]
        return buttons


class DataSettings(InterfaceData):
    def __init__(self):
        super().__init__()
        self.__count_elem = 4

    def buttons(self):
        position_audio = (
            self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 1))
        position_video = (
            self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 2))
        position_text = (self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 3))
        position_back = (self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 4))

        audio_button = Button(position_audio, self.get_size_button(), text='Audio', name='audio',
                              img_path=self._button_img)
        video_button = Button(position_video, self.get_size_button(), text='Video', name='video',
                              img_path=self._button_img)
        text_button = Button(position_text, self.get_size_button(), text='Text', name='text',
                             img_path=self._button_img)
        back_button = Button(position_back, self.get_size_button(), text='Back', name='back',
                             img_path=self._button_img)

        settings_menu_buttons = [audio_button, video_button, text_button, back_button]
        return settings_menu_buttons


class DataMainMenu(InterfaceData):
    def __init__(self):
        super().__init__()
        self.__background = f'images/{SavesSettings().get_screen_status()[-1]}/main_menu_background.png'
        self.__count_elem = 4

    def get_background_img(self):
        return self.__background

    def buttons(self):
        position_new_game = (
            self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 1))
        position_load = (self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 2))
        position_settings = (
            self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 3))
        position_quit = (self.position_in_the_center_button(), self.arrange_evenly_vert(self.__count_elem, 4))

        new_game = Button(position_new_game, self.get_size_button(), text='New game', name='new_game',
                          img_path=self._button_img)
        load_game = Button(position_load, self.get_size_button(), text='Continue', name='continue_game',
                           img_path=self._button_img)
        settings = Button(position_settings, self.get_size_button(), text='Settings', name='settings',
                          img_path=self._button_img)
        quit = Button(position_quit, self.get_size_button(), text='Quit', name='quit', img_path=self._button_img)
        main_menu_buttons = [new_game, load_game, settings, quit]
        return main_menu_buttons
