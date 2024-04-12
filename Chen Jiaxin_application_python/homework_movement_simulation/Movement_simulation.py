# coding = utf-8
import numpy as np
import matplotlib.pyplot as plt
import os

G = 9.8


class Simulation:
    def __init__(self, vx0, vy0, t0):
        self.t = np.linspace(0, t0, t0 + 1)
        self.vx = vx0 - G * self.t
        self.x = vx0 * self.t - 0.5 * G * self.t ** 2
        self.y = vy0 * self.t

    def ver_mov(self):
        print(f'The vertical movement simulation data is (1 sec interval): \n {self.x}')

    def save_rel(self):
        f = open('simulation_data.txt', 'w')
        f.write(f't: {self.t}\n')
        f.write(f'x: {self.x}\n')
        f.write(f'y: {self.y}\n')
        f.write(f'vx: {self.vx}\n')
        f.close()

    def draw_pic(self):
        plt.plot(self.y, self.x)
        plt.xlabel('y')
        plt.ylabel('x')
        plt.title('Movement Simulation')
        plt.show()


if __name__ == '__main__':
    init_vx = eval(input('Please input initial vertical speed:'))
    init_vy = eval(input('Please input initial horizontal speed:'))
    t = eval(input('Please input simulation time:'))
    s = Simulation(init_vx, init_vy, t)
    s.save_rel()
    s.ver_mov()
    s.draw_pic()
