#!usr/bin/python
# -*-coding: utf8 -*-

import pyglet
import math
from pyglet.window import Window
from pyglet.window import key
from pyglet import clock

import tank
import chassis
import turret

class GameWindow(pyglet.window.Window):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
    
    player_tank = []
    piece_of_tank = {}
    tank_1 = tank.Tank(240, 300)
    tu = turret.Turret(tank_1.x, tank_1.y)
    ch = chassis.Chassis(tank_1.x, tank_1.y)

    # Dict des instances du tank
    piece_of_tank['tank'] = tank_1
    piece_of_tank['turret'] = tu
    piece_of_tank['chassis'] = ch

    # Creation des sprites
    chassis_1 = ch.create_chassis('assets/sprites/chassis_2.png')
    turret_1 = tu.create_turret("assets/sprites/turret_2.png")

    # liste des sprites
    player_tank.append(chassis_1)
    player_tank.append(turret_1)


    def on_draw(self): # Surcharge la methode de on_draw de la superclass pyglet.window.Window
        self.clear()
        # boucle sur liste des sprites
        for t in self.player_tank:
            t.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = int(float(x))
        self.mouse_y = int(float(y))


    def on_key_press(self, symbol, modifiers):
        self.player.isKeyPressed = True
        if symbol == key.Z:
            self.direction = 'head'
        elif symbol == key.S:
            self.direction = 'back'
        elif symbol == key.D:
            self.direction = 'right'
        elif symbol == key.Q:
            self.direction = 'left'
        

    def on_key_release(self, symbol, modifiers):
        self.player.isKeyPressed = False
        self.direction = "none"


    def update(self, dt):
        self.tu.rotate(dt)
        
    
if __name__ == "__main__":
    window = GameWindow(800, 600, "Tank Yu", resizable=False)
    clock.set_fps_limit(60)
    pyglet.clock.schedule_interval(window.update, 1/60.0)
    pyglet.app.run()