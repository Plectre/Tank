# -*-coding:utf8-*-
import pyglet
import tank
import chassis

class Turret(tank.Tank):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ang = 0
        self.turret = None
        self.speed = 100
        

    def create_turret(self, img):
        turret_img = pyglet.image.load(img)
        turret_img.anchor_x = 18
        turret_img.anchor_y = 28
        self.turret = pyglet.sprite.Sprite(turret_img, self.x + 32, self.y + 42)
        return self.turret

    def rotate(self, dt):
        self.turret.rotation += self.speed * dt

    def draw(self):
        self.turret.draw()
        pass