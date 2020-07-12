import pygame


class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = 'default'
        self.frames = {
            'default': [pygame.image.load(
                f'assets/sprites/cat/default/frame-{frame_num}.png'
            ) for frame_num in range(4)],
            'moving_right': [pygame.image.load(
                f'assets/sprites/cat/moving_right/frame-{frame_num}.png'
            ) for frame_num in range(1)],
            'moving_left': [pygame.image.load(
                f'assets/sprites/cat/moving_left/frame-{frame_num}.png'
            ) for frame_num in range(1)],
        }
        self.frames_num = {
            'default': 4,
            'moving_left': 1,
            'moving_right': 1,
        }
        self.rect = pygame.Rect(100, 150, 10, 10)
        self.current_frame = 0
        self.counter = 0
        self.speed = 10
        self.max_count = self.frames_num[self.state] * self.speed

    def build(self, window):
        window.blit(self.frames[self.state][self.current_frame], (self.rect.x, self.rect.y))
        if self.counter == self.max_count:
            self.counter = 0
        else:
            self.current_frame = self.counter // self.speed
            self.counter += 1

    def process(self, button_events):
        if self.state == 'default':
            if button_events.get('276d'):
                self.state = 'moving_left'
                self.current_frame = 0
                self.counter = 0
                self.max_count = 10
            elif button_events.get('275d'):
                self.state = 'moving_right'
                self.current_frame = 0
                self.counter = 0
                self.max_count = 10
        elif self.state == 'moving_left':
            if button_events.get('276u'):
                self.state = 'default'
                self.current_frame = 0
                self.counter = 0
                self.max_count = 40
            else:
                self.rect.x -= 15
        elif self.state == 'moving_right':
            if button_events.get('275u'):
                self.state = 'default'
                self.state = 'default'
                self.current_frame = 0
                self.counter = 0
                self.max_count = 40
            else:
                self.rect.x += 15
