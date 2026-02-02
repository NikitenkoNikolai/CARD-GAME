import pygame
from color import Colors
from data_base import SavesSettings


class Button:
    def __init__(self, position: tuple[float, float], size: tuple[float, float], name=None, text=None, img_path=None,
                 img_path_push=None, description_text=None, description_text_size=None,
                 description_text_color=Colors.white(), description_pos=None):
        self.pos_x, self.pos_y = position[0], position[1]
        self.width, self.height = size[0], size[1]
        self.name = name
        self.text = text
        self.description_text = description_text
        self.description_text_color = description_text_color
        self.description_text_size = description_text_size
        self.description_pos = description_pos
        self.img_path = img_path
        self.img_path_push = img_path_push
        self.img = None

    def get_info_rect_button(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def get_info_button(self):
        return [self.pos_x, self.pos_y, self.width, self.height, self.text, self.name]

    def get_style_button(self):
        if not self.img_path:
            self.img = None
        else:
            columns = {'full_screen_box': 3, 'window_screen_box': 4, 'full_screen': 5, 'window_screen': 6}
            values = SavesSettings().get_data_settings()
            if self.name == 'full_screen_box' or self.name == 'window_screen_box':
                if values[columns[self.name]]:
                    self.img = pygame.image.load(self.img_path_push)
                    self.img = pygame.transform.scale(self.img, (self.width, self.height))
                    return self.img

            self.img = pygame.image.load(self.img_path)
            self.img = pygame.transform.scale(self.img, (self.width, self.height))
        return self.img

    def draw(self, display_window):
        self.img = self.get_style_button()
        white = Colors.white()
        black = Colors.black()
        font_size_button = int(self.height // 1.5)
        font_size_description = int(self.width * 2)
        if self.description_text_size:
            font_size_description = self.description_text_size
        if self.img:
            rect = self.img.get_rect(topleft=(self.pos_x, self.pos_y))
            current_img = self.img
            display_window.blit(current_img, rect.topleft)
        else:
            black = Colors.black()
            pygame.draw.rect(display_window, black, (self.pos_x, self.pos_y, self.width, self.height))
        if self.text:
            font = pygame.font.Font(None, font_size_button)
            text_surface = font.render(self.text, True, white)
            center = (self.pos_x + self.width // 2, self.pos_y + self.height // 2)
            text_rect = text_surface.get_rect(center=center)
            display_window.blit(text_surface, text_rect)

        if self.description_text and self.description_pos:
            font = pygame.font.Font(None, font_size_description)
            text_surface = font.render(self.description_text, True, self.description_text_color)
            center = self.description_pos
            text_rect = text_surface.get_rect(center=center)
            display_window.blit(text_surface, text_rect)


class Slider:
    def __init__(self, position: tuple[float, float], size_bond: tuple[float, float], size_point, name=None,
                 img_point=None, img_bond=None, description_text=None, description_pos=None):
        self.pos_x, self.pos_y = position[0], position[1]
        self.width_bond, self.height_bond = size_bond[0], size_bond[1]
        self.width_point, self.height_point = size_point[0], size_point[1]
        self.name = name
        self.description_text = description_text
        self.description_pos = description_pos

        if img_bond:
            self.img_bond = pygame.image.load(img_bond)
            self.img_bond = pygame.transform.scale(self.img_bond, size_bond)
        else:
            self.img_bond = None

        if img_point:
            self.img_point = pygame.image.load(img_point)
            self.img_point = pygame.transform.scale(self.img_point, size_point)
        else:
            self.img_point = None

    def get_info_rect_bond(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width_bond, self.height_bond)

    def get_info_point(self):
        return [self.pos_x, self.pos_y, self.width_point, self.height_point, self.name]

    def get_pos_point_x(self, pos_point_x=None, name_point=None):
        columns = {'audio_all': 0, 'audio_music': 1, 'audio_effects': 2, 'full_screen': 3, 'window_screen': 4}
        values = SavesSettings().get_data_settings()
        if values[columns[self.name]] == 'None':
            level_sound = self.width_bond // 2.1
            SavesSettings().save_data_settings(self.name, level_sound)

        if pos_point_x and name_point == self.name:
            level_sound_pixel = pos_point_x - self.pos_x
            level_sound_percent = level_sound_pixel * 100 / self.width_bond
            SavesSettings().save_data_settings(name_point, level_sound_percent)
        pos_point_x = self.pos_x + self.width_bond * values[columns[self.name]] / 100

        return pos_point_x

    def draw(self, display_window, pos_point_x=None, name_point=None):
        pos_point_x = self.get_pos_point_x(pos_point_x=pos_point_x, name_point=name_point)
        black = Colors.black()
        white = Colors.white()
        red = Colors.red()
        font_size = 60

        if self.description_text:
            font = pygame.font.Font(None, font_size)
            text_surface = font.render(self.description_text, True, white)
            center = self.description_pos
            text_rect = text_surface.get_rect(center=center)
            display_window.blit(text_surface, text_rect)

        if self.img_point and self.img_bond:
            rect_point = self.img_point.get_rect(topleft=(pos_point_x, self.pos_y - 30))
            rect_bond = self.img_point.get_rect(topleft=(self.pos_x, self.pos_y))
            current_img_point = self.img_point
            current_img_bond = self.img_bond
            display_window.blit(current_img_bond, rect_bond.topleft)
            display_window.blit(current_img_point, rect_point.topleft)
        else:
            pygame.draw.rect(display_window, black, (self.pos_x, self.pos_y, self.width_bond, self.height_bond))
            pygame.draw.rect(display_window, red,
                             (pos_point_x, self.pos_y, self.width_point, self.height_point))
