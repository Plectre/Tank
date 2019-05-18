# -*-coding:utf8-*-
import tank
import pyglet

class Chassis(tank.Tank):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.chassis = None
        self.size = 0

    def create_chassis(self, img):
        chassis_img = pyglet.image.load(img)
        self.chassis = pyglet.sprite.Sprite(chassis_img, self.x, self.y)
        return self.chassis

    def rotate(self, rot):
        self.spr_chassis.rotation  = rot

    def draw():
        self.chassis.draw()