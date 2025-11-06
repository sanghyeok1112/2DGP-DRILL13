from pico2d import *

import game_world


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 1600, 60

    def handle_collision(self, group, other):
        if group == 'grass:ball':
            game_world.remove_object(self)
        elif group == 'grass:ball':
            self.stopped = True
