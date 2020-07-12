from common.objects import Sprite


class GameObjectsCreator:
    def __init__(self, game_globals, game_objects):
        self.game_globals = game_globals
        self.game_objects = game_objects

    def check_objects_for_create(self):
        if self.game_globals.should_make_colored_sprites:
            self.game_objects.first_layer.append(Sprite(
                position_x=100,
                position_y=80,
                width=64,
                height=64,
                image_asset='assets/bad-fire-sprite.png',
            ))
            self.game_objects.second_layer.append(Sprite(
                position_x=20,
                position_y=80,
                width=64,
                height=64,
                image_asset='assets/black-red-sprite.png',
            ))
            self.game_objects.third_layer.append(Sprite(
                position_x=20,
                position_y=60,
                width=64,
                height=64,
                image_asset='assets/black-green-sprite.png',
            ))
            self.game_objects.fourth_layer.append(Sprite(
                position_x=20,
                position_y=40,
                width=64,
                height=64,
                image_asset='assets/black-blue-sprite.png',
            ))
            self.game_objects.fifth_layer.append(Sprite(
                position_x=20,
                position_y=20,
                width=64,
                height=64,
                image_asset='assets/black-white-sprite.png',
            ))

            self.game_globals.should_make_colored_sprites = False
