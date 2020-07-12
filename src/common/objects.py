import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, width, height, image_asset):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.scale_image(image_asset)
        self.rect = pygame.Rect(position_x, position_y, width, height)

    def build(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def scale_image(self, image_asset):
        image = pygame.image.load(image_asset)
        return pygame.transform.scale(image, (image.get_width()*4, image.get_height()*4))


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, width, height, animation_asset, frames_num, speed=1):
        pygame.sprite.Sprite.__init__(self)
        self.frames = [
            pygame.image.load(
                f'assets/sprites/{animation_asset}/frame-{frame_num}.png'
            ) for frame_num in range(frames_num)
        ]
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.current_frame = 0
        self.counter = 0
        self.speed = speed
        self.max_count = frames_num * self.speed

    def build(self, window):
        window.blit(self.frames[self.current_frame], (self.rect.x, self.rect.y))
        if self.counter == self.max_count:
            self.counter = 0
        else:
            self.current_frame = self.counter // self.speed
            self.counter += 1


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
