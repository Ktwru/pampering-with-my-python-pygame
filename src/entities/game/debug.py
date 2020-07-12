import pygame
import params
from common.objects import Font


class Debugger:
    def __init__(self, window):
        self.window = window
        self.position_x = params.DEBUG_POSITION[0]
        self.position_y = params.DEBUG_POSITION[1]
        self.input = Font(text='input:', position_x=self.position_x, position_y=self.position_y+16, size=16)
        self.input_active = False
        self.map_name = Font(text='map:', position_x=self.position_x, position_y=self.position_y+32, size=16)
        self.buttons = Font(text='buttons:', position_x=self.position_x-600, position_y=self.position_y, size=14)

    def watch(self, events, game_globals):
        button_events = events.get('button')
        if button_events:
            self.perform_buttons(button_events)
            self.perform_input(button_events=button_events, game_globals=game_globals)
        self.perform_map(game_globals.map_name)
        self.buttons.build(self.window)
        self.input.build(self.window)
        self.map_name.build(self.window)

    def perform_buttons(self, button_events):
        self.buttons.text = 'buttons:' + ','.join(button_events.keys())

    def perform_input(self, button_events, game_globals):
        if button_events.get('`'):
            if self.input_active:
                self.input.text = 'input:'
            else:
                self.input.text = 'input!:'
            self.input_active = not self.input_active
        if self.input_active:
            if button_events.get('m'):
                self.input.text = 'input!:m'
                game_globals.map_name = 'another_map'
                return

    def perform_map(self, map_name):
        self.map_name.text = 'map:' + map_name
