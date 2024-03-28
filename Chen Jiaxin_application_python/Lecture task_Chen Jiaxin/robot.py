# coding = utf-8
"""
author：
Chen Jiaxin

software engineering
"""
import math


class Robot:
    def __init__(self, x: object = 0, y: object = 0, angle: object = 0) -> object:
        self.x = x
        self.y = y
        self.angle = angle
        self.status = 'null'

    def open(self):
        self.status = 'open'

    def forward(self, distance):
        if self.status == 'open':
            self.x += distance * math.cos(self.angle)
            self.y += distance * math.sin(self.angle)
            print(f'The robot went forward {distance}')
        else:
            print('The robot has not open!')

    def rotate(self, angle):
        if self.status == 'open':
            self.angle += angle
            print(f'The robot rotated {angle}')
        else:
            print('The robot has not open!')

    def stop(self):
        self.status = 'stop'

    def show(self):
        print(f'The location is ({self.x} , {self.y})\nThe angle is {self.angle}')

