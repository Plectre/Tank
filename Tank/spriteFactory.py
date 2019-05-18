import pyglet
import math
from random import randint

class TankFactory():
    def __init__(self, img, img2):
        self.img = img
        self.img2 = img2
        self.sprite = None
        self.sprite_2 = None
        self.tank = []
        self.pos_x = randint(50, 550)
        self.pos_y = 400
        self.speed = 50
        self.isKeyPressed = False
        self.chassis_angle = 0
        self.angle = 0
        pass


    def makeTank(self):

        img_sprite = pyglet.image.load(self.img)
        img2_sprite = pyglet.image.load(self.img2)
        img_sprite.anchor_x=32
        img_sprite.anchor_y=42
        img2_sprite.anchor_x=19
        img2_sprite.anchor_y=22
        self.sprite = pyglet.sprite.Sprite(img_sprite, self.pos_x, self.pos_y)
        self.sprite_2 = pyglet.sprite.Sprite(img2_sprite, self.pos_x, self.pos_y)
        self.tank.append(self.sprite)
        self.tank.append(self.sprite_2)
        #return tank

    def draw(self):
        self.tank[0].draw()
        self.tank[1].draw()

    def rotation(self, mouse_x, mouse_y):
        self.angle = math.atan2(mouse_y - self.pos_y , mouse_x - self.pos_x)
        rotation = (180 * self.angle / math.pi) * -1
        if rotation > 360:
            rotation = 0
        self.tank[1].rotation = rotation

    def direction(self, dir, dt):
        if self.isKeyPressed:
            if dir == 'head':
                self.tank[0].y += dt * self.speed
                self.tank[1].y += dt * self.speed
            if dir == 'back':
                self.tank[0].y -= dt * self.speed
                self.tank[1].y -= dt * self.speed
            if dir == 'right':
                self.tank[0].rotation += 2
                if self.tank[0].rotation > 359:
                    self.tank[0].rotation = 0
                print(self.tank[0].rotation)
            if dir == 'left':
                self.tank[0].rotation -= 2
                if self.tank[0].rotation < 0:
                    self.tank[0].rotation = 359
                #print(self.tank[0].rotation)
