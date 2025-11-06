import random
from pico2d import *

import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    zombie = [Zombie() for _ in range(5)]
    game_world.add_objects(zombie, 1)



    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_collision_pairs('grass:ball', grass, None)

    boy = Boy()
    game_world.add_object(boy, 1)

    global balls
    balls = [Ball(random.randint(200, 1600), 60, 0) for _ in range(20)]
    game_world.add_objects(balls, 1)

    game_world.add_collision_pairs('boy:balls', boy, None)
    for ball in balls:
        game_world.add_collision_pairs('ball:grass', None, ball)






def update():
    game_world.update()
    handle_collision()




def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

def handle_collision():
    for group, pairs in game_world.collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if game_world.collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)