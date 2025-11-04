from pico2d import *
import random

import game_framework

PIXEL_PER_METER = (10.0 / 1.7) # 10 pixel 30 cm
RUN_SPEED_KMPH = 80.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.image_x = 918
        self.image_y = 516
        self.x = random.randint(100, 500)
        self.y = random.randint(300, 500)
        self.size_x=173
        self.size_y=162
        self.frame=0
        self.dir=1

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 100:
            self.dir = 1

        pass

    def draw(self):
        self.image.clip_composite_draw(int(self.frame)%5 * int(self.image_x/5),(2-int(self.frame) // 5) *int(self.image_y/3), self.size_x, self.size_y,0,'' if self.dir==1 else 'h', self.x, self.y,100,100)

