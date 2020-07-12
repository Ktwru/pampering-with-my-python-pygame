import sys

import pygame

import params
from dataclasses import dataclass
from entities.game.debug import Debugger
from entities.game.game_controller import GameController


class Game:
    def __init__(self):
        pygame.init()
        self.window = self.build_window()
        self.clock = pygame.time.Clock()

        self.event_listener = EventListener()

        self.globals = Globals(
            map_name='mppp',
            debug_mode=params.DEBUG_MODE,
            should_make_colored_sprites=True,
        )
        self.game_objects = GameObjects(
            first_layer=[],
            second_layer=[],
            third_layer=[],
            fourth_layer=[],
            fifth_layer=[],
        )

        self.game_controller = GameController(game_globals=self.globals, game_objects=self.game_objects)

        self.debugger = Debugger(window=self.window, game_globals=self.globals, clock=self.clock)

    def build_window(self):
        window = pygame.display.set_mode(size=(params.WINDOW_HEIGHT, params.WINDOW_WIDTH))
        pygame.display.set_caption(params.WINDOW_CAPTION)
        window.fill((0, 0, 0))
        return window

    def handle_tic(self):
        self.window.fill((0, 0, 0))  # todo

        events = self.event_listener.check_for_events()

        self.game_controller.process()

        self.game_objects.build_all(self.window)

        if self.globals.debug_mode:
            self.debugger.watch(events=events)

        pygame.display.update()
        self.clock.tick(30)     # todo i doesnt know what i should do
        # pygame.time.delay(params.TIME_DELAY)


class EventListener:
    def check_for_events(self):
        events = pygame.event.get()
        events_dict = {'button': {}, 'other': []}
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == 2:    # todo - writing only 2:keyUp and 3:keyDown
                events_dict['button'][str(event.key)+'d'] = event
            elif event.type == 3:
                events_dict['button'][str(event.key)+'u'] = event
            else:
                events_dict['other'].append(event)
        return events_dict

    def quit(self):
        pygame.quit()
        sys.exit()


@dataclass
class Globals:
    map_name: str = None
    debug_mode: bool = False
    should_make_colored_sprites: bool = False
    should_remove_colored_sprites: bool = False


@dataclass
class GameObjects:
    first_layer: list = None
    second_layer: list = None
    third_layer: list = None
    fourth_layer: list = None
    fifth_layer: list = None

    def build_all(self, window):
        for layer in [self.fifth_layer, self.fourth_layer, self.third_layer, self.second_layer, self.first_layer]:
            for game_object in layer:
                game_object.build(window)
