import params
from common.objects import Font, Sprite


class Debugger:
    def __init__(self, window, game_globals, clock):
        self.window = window
        self.clock = clock
        self.position_x = params.DEBUG_POSITION[0]
        self.position_y = params.DEBUG_POSITION[1]
        self.game_globals = game_globals

        self.should_execute_in_next_tick = False
        self.input_active = False
        self.input = Font(text='input:', position_x=self.position_x-600, position_y=self.position_y+16, size=16)
        self.input_value = Font(text='', position_x=self.position_x-560, position_y=self.position_y+16, size=16)
        self.map_name = Font(text='map:', position_x=self.position_x, position_y=self.position_y+32, size=16)
        self.fps = Font(text='fps:', position_x=self.position_x, position_y=self.position_y+48, size=16)
        self.buttons = Font(text='buttons:', position_x=self.position_x-600, position_y=self.position_y, size=14)

    def watch(self, events):
        button_events = events.get('button')
        if button_events or self.should_execute_in_next_tick:
            self.perform_buttons(button_events)
            self.perform_input(button_events)
        self.perform_map()
        self.perform_fps()

        self.buttons.build(self.window)
        self.input.build(self.window)
        self.input_value.build(self.window)
        self.map_name.build(self.window)
        self.fps.build(self.window)

    def perform_buttons(self, button_events):
        self.buttons.text = 'buttons:' + ','.join(button_events.keys())

    def perform_input(self, button_events):
        if button_events.get('96d'):
            if self.input_active:
                self.input_value.text = ''
            else:
                self.input_value.text = '!'
            self.input_active = not self.input_active
            return
        if self.input_active:
            if button_events.get('8d'):
                self.input_value.text = '!'
            elif button_events.get('13d') or self.should_execute_in_next_tick:
                self.execute_command()
            else:
                event = list(button_events.values())[0]
                if hasattr(event, 'unicode'):
                    self.input_value.text += event.unicode

    def execute_command(self):
        if 'globals:' in self.input_value.text:     # globals:var_name:var_value
            cmd = self.input_value.text.split(':')
            if cmd[2] == 'false':
                cmd[2] = False
            elif cmd[2] == 'true':
                cmd[2] = True
            setattr(self.game_globals, cmd[1], cmd[2])
            self.input_value.text = '!'
        elif 'test_computations:' in self.input_value.text:     # test_computations:val1:val2:iterations:ticks
            self.should_execute_in_next_tick = True
            cmd = self.input_value.text.split(':')
            tick = int(cmd[4])
            if tick == 0:
                self.input_value.text = '!'
                self.should_execute_in_next_tick = False
            else:
                val1 = int(cmd[1])
                val2 = int(cmd[2])
                for iteration in range(int(cmd[3])):
                    val1 += val2
                self.input_value.text = f'{cmd[0]}:{cmd[1]}:{cmd[2]}:{cmd[3]}:{tick-1}'
        elif 'test_sprite_builds:' in self.input_value.text:    # test_sprite_builds:sprite_asset:iterations:ticks
            self.should_execute_in_next_tick = True
            cmd = self.input_value.text.split(':')
            tick = int(cmd[3])
            if tick == 0:
                self.input_value.text = '!'
                self.should_execute_in_next_tick = False
            else:
                for iteration in range(int(cmd[2])):
                    sprite = Sprite(250, 250, 10, 10, cmd[1])
                    sprite.build(self.window)
                self.input_value.text = f'{cmd[0]}:{cmd[1]}:{cmd[2]}:{tick-1}'

    def perform_map(self):
        self.map_name.text = 'map:' + self.game_globals.map_name

    def perform_fps(self):
        self.fps.text = 'fps:' + str(int(self.clock.get_fps()))
