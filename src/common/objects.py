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


class Font:
    def __init__(
            self,
            text,
            position_x,
            position_y,
            font_asset='assets/fonts/PixelFont.ttf',
            size=24,
            color=(0, 135, 72),
    ):
        self.font = pygame.font.Font(font_asset, size)
        self.position_x = position_x
        self.position_y = position_y
        self.text = text
        self.color = color

    def build(self, window):
        title = self.font.render(self.text, 0, self.color)
        window.blit(title, (self.position_x, self.position_y))
