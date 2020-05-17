# Simple CA simulator in Python
#
# *** Hosts & Pathogens ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

# Modified to run with Python 3

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 50
height = 50
initProb = 0.2
infectionRate = 0.85
regrowthRate = 0.15

def init():
    global time, config, nextConfig

    time = 0
    
    config = SP.zeros([height, width])
    for x in range(width):
        for y in range(height):
            if RD.random() < initProb:
                state = 2
            else:
                state = 1
            config[y, x] = state

    nextConfig = SP.zeros([height, width])

def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 2, cmap = PL.cm.jet)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, config, nextConfig

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            if state == 0:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == 1:
                            if RD.random() < regrowthRate:
                                state = 1
            elif state == 1:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == 2:
                            if RD.random() < infectionRate:
                                state = 2
            else:
                state = 0

            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

"""#interative
import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])"""

#non-interactive
def count_prop(config):
    healthy = 0
    infected = 0
    for x in range(width):
        for y in range(height):
            if config[x,y] == 1:
                healthy += 1
            if config[x,y] == 2:
                infected += 1
    return healthy/2500, infected/2500, infected/healthy

h = []
i = []
ih = []

init()
prop_h, prop_i, prop_ih = count_prop(config)
h.append(prop_h)
i.append(prop_i)
ih.append(prop_ih)
while time<500:
    step()
    prop_h, prop_i, prop_ih = count_prop(config)
    h.append(prop_h)
    i.append(prop_i)
    ih.append(prop_ih)

time_span = np.array(range(0,501))
plt.plot(time_span,i)
plt.plot(time_span,h)
plt.xlabel('Time')
plt.ylabel('No. of infected / No. of healthy')
plt.show()

