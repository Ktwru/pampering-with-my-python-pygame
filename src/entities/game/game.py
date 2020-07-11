import sys

import pygame

import params
from dataclasses import dataclass
from entities.map.map_builder import MapBuilder


class Game:
    def __init__(self):
        pygame.init()
        self.window = self.build_window()
        self.event_listener = EventListener()
        self.map_builder = MapBuilder(window=self.window)

        self.globals = Globals(map_name='mppp')

    def build_window(self):
        window = pygame.display.set_mode(size=(params.WINDOW_HEIGHT, params.WINDOW_WIDTH))
        pygame.display.set_caption(params.WINDOW_CAPTION)
        window.fill((0, 0, 0))
        return window

    def handle_tic(self):
        self.event_listener.check_for_events()
        self.map_builder.check_current_map(current_map_name=self.globals.map_name)
        pygame.display.update()
        pygame.time.delay(params.TIME_DELAY)


class EventListener:
    def check_for_events(self):
        events = pygame.event.get()
        for event in events:
            self.handle_event(event=event)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


@dataclass
class Globals:
    map_name: str = None
