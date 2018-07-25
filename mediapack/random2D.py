# coding: utf-8

"""
Explain WTF your doing
"""

import matplotlib.pyplot as plt
import numpy as np
import ezdxf

__author__ = 'George Pamfilis'

class MediaGenerator(object):
    pass

class Random2DIsotropic(object):
    def __init__(self, height=[0., 20.], width=[0., 200.], radius_range=[0.5, .1], number_of_particles=60.,
                 fname='test.png', grain_dist='norm'):
        self.height = height
        self.width = width
        self.radius_range = radius_range
        self.number_of_particles = number_of_particles
        self.fname = fname
        self.grain_dist=grain_dist
        self.margin = 2
        self.offset=None

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

    def compute_porosity(self):
        xx,yy,rr = self.create_random_porous_media_normal()
        return theta


    def draw_media(self):
        if self.grain_dist == 'norm':
            xx, yy, rr = self.create_random_porous_media_normal()
        else:
            xx, yy, rr = self.create_random_porous_media_uniform()
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
        plt.savefig(self.fname)
        return xx, yy, rr

    def export_dfx(self):
        xx,yy,rr = self.draw_media()
        self.offset = np.max(rr)

        width = self.width[1]#+(2*self.offset*self.margin)
        height = self.height[1]#t+(2*self.offset*self.margin)

        dwg = ezdxf.new('AC1015')
        dwg.layers.new(name='frame')
        dwg.layers.new(name='media')

        msp = dwg.modelspace()

        points = [(0,0), (width,0), (width,height), (0, height),(0,0)]
        msp.add_lwpolyline(points, dxfattribs={'layer':'frame'})
        #
        for j in range(xx.shape[0]):
            for i in range(xx[j].shape[0]):
                msp.add_circle((xx[j][i],yy[j][i]),rr[i][j], dxfattribs={'layer':'media'})
        dwg.saveas('/home/kasper/Dropbox/SHARED PROJECTS/random_media.dxf')

class Random2DIsotropic2(object):
    def __init__(self, height=[0., 20.], width=[0., 200.], radius_range=[0.5, .1], nx=60, ny=50,number_of_particles=10,
                 fname='test.png', grain_dist='norm'):
        self.height = height
        self.width = width
        self.radius_range = radius_range
        self.number_of_particles = number_of_particles
        self.fname = fname
        self.grain_dist=grain_dist
        self.margin = 2
        self.offset=None
        self.nx=nx
        self.ny=ny
        self.theta = None

    def create_random_porous_media_uniform(self):
        x,y = np.linspace(*self.width, num=self.nx), np.linspace(*self.height, num=self.ny)


        xx, yy = np.meshgrid(x,y)
        print(xx.shape)
        print(yy.shape)

        #shift x to the right every two
        # for i in range(0,xx.shape[0],2):
        #     print(i)
        #     xx[i] = xx[i]+(self.width[1]/self.nx)/2

        #shift y to the right every two
        for i in range(0,xx.shape[0]):
            for j in range(0,yy[i].shape[0],2):
                yy[i][j] = yy[i][j]+(self.height[1]/self.ny)/2
        rr = np.random.uniform(self.radius_range[0], self.radius_range[1], (self.nx, self.ny))
        return xx, yy, rr


    def compute_porosity(self, rr):
        totalV = self.width[1]*self.height[1]
        print(np.pi)
        partials = []
        for r in rr:
            partial = np.sum(np.pi*r**2)
            partials.append(partial)
        grain_area = sum(partials)
        print(grain_area)
        print(totalV)
        theta= (totalV-grain_area)/totalV
        print(theta)
        return theta


    def draw_media(self, xx,yy,rr):
        # if self.grain_dist == 'norm':
        #     xx, yy, rr = self.create_random_porous_media_normal()
        # else:
        # xx, yy, rr = self.create_random_porous_media_uniform()
        self.theta = self.compute_porosity(rr)
        # for i in range(xx[0].shape[0]):


        plt.figure(figsize=(20, 20 * (self.height[1] / self.width[1])))
        fig = plt.gcf()
        for j in range(xx.shape[0]):
            for i in range(xx[j].shape[0]):
                circle1 = plt.Circle((xx[j][i], yy[j][i]), rr[i][j], color='r')
                fig.gca().add_artist(circle1)
        # fig.show()
        # fig.show()
        ad = 0#np.max(rr)*self.margin*2
        plt.xlim(0-ad, self.width[1]+ad)
        plt.ylim(0-ad, self.height[1]+ad)
        plt.show()
        # plt.savefig(self.fname)
        return xx, yy, rr

    def gerate_given_porosity(self, porosity):

        while porosity>theta:
            theta = self.compute_porosity(rr)
        pass


    def export_dfx(self):
        xx, yy, rr = self.create_random_porous_media_uniform()
        # self.draw_media(xx, yy, rr)
        # xx, yy, rr = self.create_random_porous_media_uniform()
        self.theta = self.compute_porosity(rr)

        self.offset = np.max(rr)
        width = self.width[1]#+(2*self.offset*self.margin)
        height = self.height[1]#t+(2*self.offset*self.margin)

        dwg = ezdxf.new('AC1015')
        dwg.layers.new(name='frame')
        dwg.layers.new(name='media')
        msp = dwg.modelspace()

        # points = [(0-self.offset,0), (width+self.offset,0), (width+self.offset,height), (0-self.offset, height),(0-self.offset,0)]
        points = [(0,0), (width+(2.5*self.offset), 0), (width+(2.5*self.offset), height), (0, height),(0,0)]

        msp.add_lwpolyline(points, dxfattribs={'layer':'frame'})
        #
        for j in range(xx.shape[0]):
            for i in range(xx[j].shape[0]):
                msp.add_circle((xx[j][i]+self.offset, yy[j][i]), rr[i][j], dxfattribs={'layer':'media'})
        # TODO: add datetime to media name
        dwg.saveas('/home/kasper/Dropbox/SHARED PROJECTS/random_media_'+str(round(self.theta,2))+'w_'+str(width)+'_h_'+str(height)+'.dxf')
        return self.theta


if __name__ == '__main__':
    # default values
    # height = [0, 25]
    # width = [0, 200]
    # radius_range = [0.25, 0.6]
    # number_of_particles = 10
    # nx=160
    # ny=20
    factorx = 1
    factory = 1
    height = [0, 25*factory]
    width = [0, 200*factorx]
    radius_range = [0.25, 0.25]
    # number_of_particles = 10
    nx=(160*factorx)+200
    ny=20*factory + 10
    # Random2DIsotropic2(height, width, radius_range, number_of_particles).export_dfx()
    # Random2DIsotropic2(height, width, radius_range, nx, ny).export_dfx()
    media = Random2DIsotropic2(height, width, radius_range, nx, ny)
    a = media.create_random_porous_media_uniform()
    # media.draw_media(*a)

    print(media.compute_porosity(a[-1]))
    media.export_dfx()
    # media.draw_media(*a)
    # for r in np.linspace(0.25,0.5,10):
    #     Random2DIsotropic(height, width, [r,0.6], nx, ny).export_dfx()


    # Random2DIsotropic(height, width, radius_range, nx, ny).compute_porosity()
