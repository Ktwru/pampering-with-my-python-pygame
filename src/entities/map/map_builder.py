import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, width, height, image_asset):
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.position_y = position_y
        self.image = pygame.image.load(image_asset)
        self.rect = pygame.Rect(position_x, position_y, width, height)

    def build(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


# class SolidSprite(Sprite):
#     def __init__(self, image: str, position_x: int, position_y: int):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image).convert_alpha()
#         self.rect = self.image.get_rect(center=(position_x, position_y))


class Map:
    def __init__(self, window):
        self.first_layer = Sprite(0, 100, 200, 200, 'assets/sprite.png')
        self.second_layer = ...
        self.third_layer = ...
        self.window = window

    def build(self):
        self.first_layer.build(window=self.window)


class MapBuilder:
    def __init__(self, window):
        self.map_name = None
        self.window = window

    def check_current_map(self, current_map_name):
        if current_map_name != self.map_name:
            self.change_map(new_map_name=current_map_name)

    def change_map(self, new_map_name):
        new_map = Map(window=self.window)
        new_map.build()
        self.map_name = new_map_name
