import sys

import pygame

import params
from dataclasses import dataclass
from entities.map.map_builder import MapBuilder
from entities.game.debug import Debugger


class Game:
    def __init__(self):
        pygame.init()
        self.window = self.build_window()
        self.event_listener = EventListener()
        self.map_builder = MapBuilder(window=self.window)
        self.debugger = Debugger(window=self.window)

        self.globals = Globals(map_name='mppp', debug_mode=params.DEBUG_MODE)

    def build_window(self):
        window = pygame.display.set_mode(size=(params.WINDOW_HEIGHT, params.WINDOW_WIDTH))
        pygame.display.set_caption(params.WINDOW_CAPTION)
        window.fill((0, 0, 0))
        return window

    def handle_tic(self):
        self.window.fill((0, 0, 0))  # todo

        events = self.event_listener.check_for_events()
        self.map_builder.check_current_map(current_map_name=self.globals.map_name)

        if self.globals.debug_mode:
            self.debugger.watch(events=events, game_globals=self.globals)

        pygame.display.update()
        pygame.time.delay(params.TIME_DELAY)


class EventListener:
    def check_for_events(self):
        events = pygame.event.get()
        events_dict = {'button': {}, 'other': []}
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == 2:    # todo - writing only 2:keyUp and 3:keyDown
                events_dict['button'][event.unicode] = event
            elif event.type == 3:
                events_dict['button'][str(event.key)] = event
            else:
                events_dict['other'].append(event)
        return events_dict

    def quit(self):
        pygame.quit()
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ...


@dataclass
class Globals:
    map_name: str = None
    debug_mode: bool = False
