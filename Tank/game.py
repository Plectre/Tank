#!usr/bin/python
# -*-coding: utf8 -*-

import pyglet
import math
from spriteFactory import TankFactory
from pyglet.window import Window
from pyglet.window import key
from pyglet import clock

sprites = []



class GameWindow(pyglet.window.Window):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.set_location(400, 100)
        self.frame_rate = 1/60.0
        self.rotation = 0
        self.posY = 0
        self.speed = 10
        self.is_pressed = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.direction = ""
        self.fps_display = clock.ClockDisplay()

    
    player = TankFactory('assets/sprites/chassis_2.png', 'assets/sprites/turret_2.png')
    mob = TankFactory('assets/sprites/chassis_2.png', 'assets/sprites/turret_2.png')
    mob2 = TankFactory('assets/sprites/chassis_2.png', 'assets/sprites/turret_2.png')
    player.makeTank()
    sprites.append(player)

    def on_draw(self): # Surcharge la methode de on_draw de la superclass pyglet.window.Window
        self.clear()
        self.fps_display.draw()
        for sprite in sprites:
            sprite.draw()

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
        self.player.rotation(self.mouse_x, self.mouse_y)
        self.player.direction(self.direction, dt)
    
if __name__ == "__main__":
    window = GameWindow(800, 600, "Tank Yu", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
