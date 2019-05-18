# -*-coding:utf8-*-
import tank
import pyglet

class Chassis(tank.Tank):
    def __init__(self, x, y):
        super.__init__(x, y)
        self.x = super().x
        self.y = super().y


    def create_chassis(self, img):
        chassis_img = pyglet.image.load(img)