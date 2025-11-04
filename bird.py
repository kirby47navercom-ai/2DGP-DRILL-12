from pico2d import *
import random

import game_framework

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.image_x = 918
        self.image_y = 516
        self.x = 100
        self.y = random.randint(300, 500)
        self.size_x=173
        self.size_y=162
        self.frame=0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        pass

    def draw(self):
        self.image.clip_composite_draw(int(self.frame)%5 * int(self.image_x/5),(2-int(self.frame) // 5) *int(self.image_y/3), int(self.image_x/5)-5, int(self.image_y/3)-10,0,'', self.x, self.y,100,100)
        print(int(self.image_x/5))

