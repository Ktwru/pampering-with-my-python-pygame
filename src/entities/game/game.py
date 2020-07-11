import sys

import pygame

import params


class Game:
    def __init__(self):
        pygame.init()
        self.window = self.build_window()
        self.event_listener = EventListener()

    def build_window(self):
        window = pygame.display.set_mode(size=(params.WINDOW_HEIGHT, params.WINDOW_WIDTH))
        pygame.display.set_caption(params.WINDOW_CAPTION)
        window.fill((0, 0, 0))
        return window

    def handle_tic(self):
        self.event_listener.check_for_events()
        pygame.display.update()


class EventListener:
    def check_for_events(self):
        events = pygame.event.get()
        for event in events:
            self.handle_event(event=event)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
