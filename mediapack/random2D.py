# coding: utf-8

"""
Explain WTF your doing
"""

import matplotlib.pyplot as plt
import numpy as np
import ezdxf

__author__ = 'George Pamfilis'


class Random2D(object):
    def __init__(self, height=[0., 25.], width=[0., 200.], radius_range=[0.5, .1], number_of_particles=60.,
                 fname='test.png', grain_dist='norm'):
        self.height = height
        self.width = width
        self.radius_range = radius_range
        self.number_of_particles = number_of_particles
        self.fname = fname
        self.grain_dist=grain_dist

    def create_random_porous_media_uniform(self):
        xx = np.random.uniform(self.width[0]+1, self.width[1]-1, (self.number_of_particles, self.number_of_particles))
        yy = np.random.uniform(self.height[0]+1, self.height[1]-1, (self.number_of_particles, self.number_of_particles))
        rr = np.random.uniform(self.radius_range[0], self.radius_range[1], (self.number_of_particles, self.number_of_particles))
        return xx, yy, rr

    def create_random_porous_media_normal(self):
        xx = np.random.uniform(self.width[0]+1, self.width[1]-1, (self.number_of_particles, self.number_of_particles))
        yy = np.random.uniform(self.height[0]+1, self.height[1]-1, (self.number_of_particles, self.number_of_particles))
        rr = np.random.normal(self.radius_range[0], self.radius_range[1], (self.number_of_particles, self.number_of_particles))
        return xx, yy, rr

    def draw_media(self):
        if self.grain_dist == 'norm':
            xx, yy, rr = self.create_random_porous_media_normal()
        else:
            xx, yy, rr = self.create_random_porous_media_uniform()
        print(xx)
        plt.figure(figsize=(20, 20 * (self.height[1] / self.width[1])))
        fig = plt.gcf()
        for j in range(xx.shape[0]):
            for i in range(xx[j].shape[0]):
                circle1 = plt.Circle((xx[j][i], yy[j][i]), rr[i][j], color='r')
                fig.gca().add_artist(circle1)
        # fig.show()
        # fig.show()
        plt.xlim(0, self.width[1])
        plt.ylim(0, self.height[1])
        plt.show()
        # plt.savefig(self.fname)
        # return fig


if __name__ == '__main__':
    height = [0, 25]
    width = [0, 200]
    radius_range = [0.5, .1]
    number_of_particles = 60
    Random2D(height, width, radius_range, number_of_particles).draw_media()
