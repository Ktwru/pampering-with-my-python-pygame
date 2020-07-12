from common.objects import Sprite, AnimatedSprite
from entities.game_objects.cat import Cat


class GameController:
    def __init__(self, game_globals, game_objects):
        self.game_globals = game_globals
        self.game_objects = game_objects

    def process(self, buttons_events):
        if self.game_globals.map_name != self.game_globals.current_map_name:
            self.game_objects.fifth_layer.append(Sprite(
                0, 0, 10, 10, f'assets/sprites/maps/{self.game_globals.map_name}/layer-5.png')
            )
            self.game_objects.fourth_layer.append(Sprite(
                0, 0, 10, 10, f'assets/sprites/maps/{self.game_globals.map_name}/layer-4.png')
            )
            self.game_objects.third_layer.append(Sprite(
                0, 0, 10, 10, f'assets/sprites/maps/{self.game_globals.map_name}/layer-3.png')
            )
            self.game_objects.second_layer.append(Sprite(
                0, 0, 10, 10, f'assets/sprites/maps/{self.game_globals.map_name}/layer-2.png')
            )
            self.game_globals.current_map_name = self.game_globals.map_name
        for game_object in self.game_objects.third_layer:
            if hasattr(game_object, 'process'):
                game_object.process(buttons_events)
        if self.game_globals.spawn_cat:
            self.game_objects.third_layer.append(Cat())
            self.game_globals.spawn_cat = False
        if self.game_globals.should_remove_colored_sprites:
            for layer in [
                self.game_objects.first_layer,
                self.game_objects.second_layer,
                self.game_objects.third_layer,
                self.game_objects.fourth_layer,
                self.game_objects.fifth_layer,
            ]:
                for game_object in layer:
                    layer.remove(game_object)
            self.game_globals.should_remove_colored_sprites = False
        if self.game_globals.should_make_colored_sprites:
            self.game_objects.first_layer.append(AnimatedSprite(
                position_x=100,
                position_y=180,
                width=64,
                height=64,
                animation_asset='bad-fire',
                frames_num=3,
                speed=4,
            ))
            self.game_objects.second_layer.append(Sprite(
                position_x=20,
                position_y=180,
                width=64,
                height=64,
                image_asset='assets/black-red-sprite.png',
            ))
            self.game_objects.third_layer.append(Sprite(
                position_x=20,
                position_y=160,
                width=64,
                height=64,
                image_asset='assets/black-green-sprite.png',
            ))
            self.game_objects.fourth_layer.append(Sprite(
                position_x=20,
                position_y=140,
                width=64,
                height=64,
                image_asset='assets/black-blue-sprite.png',
            ))
            self.game_objects.fifth_layer.append(Sprite(
                position_x=20,
                position_y=120,
                width=64,
                height=64,
                image_asset='assets/black-white-sprite.png',
            ))

            self.game_globals.should_make_colored_sprites = False
