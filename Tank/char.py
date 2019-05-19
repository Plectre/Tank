#*-* coding:utf8 *-*

import pyglet
import math

class Char():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.spr_chassis = None
        self.spr_turret = None
        self.speed = 5

    def createChar(self, img_chassis, img_turret):
        char = {}
        img_ch = pyglet.image.load(img_chassis)
        img_ch.anchor_x = 32
        img_ch.anchor_y = 42
        img_tu = pyglet.image.load(img_turret)
        img_tu.anchor_x = 32
        img_tu.anchor_y = 30
        self.spr_chassis = pyglet.sprite.Sprite(img_ch, self.x, self.y)
        self.spr_turret = pyglet.sprite.Sprite(img_tu, self.x, self.y)
        char["chassis"] = self.spr_chassis
        char["turret"] = self.spr_turret
        return char

    def move(self, dir):
        if dir == 'forward':
            self.spr_chassis.y += self.speed
            self.spr_turret.y += self.speed
        if dir == 'back':
            self.spr_chassis.y -= self.speed
            self.spr_turret.y -= self.speed

    def turret_rotate(self, x, y, mouse_x, mouse_y, dt):
        result = math.atan2(mouse_y - y , mouse_x - x)
        angle = ((180 * result / math.pi) * -1).__round__()
        self.spr_turret.rotation = angle + 90

    def chassis_rotate(self, dir):
        if dir == 'right':
            self.spr_chassis.rotation += 10
        if dir == 'left':
            self.spr_chassis.rotation -= 10


