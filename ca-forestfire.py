# Simple CA simulator in Python
#
# *** Forest fire ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

# Modified to run with Python 3

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import pylab as PL
import random as RD
import scipy as SP
import numpy as np

RD.seed()

width = 100
height = 100
initProb = 0.4
empty, tree, fire, char = range(4)

def init():
    global time, config, nextConfig

    time = 0

    config = SP.zeros([height, width])
    for x in range(width):
        for y in range(height):
            if RD.random() < initProb:
                state = tree
            else:
                state = empty
            config[y, x] = state
    config[height//2, width//2] = fire

    nextConfig = SP.zeros([height, width])

def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 3, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, config, nextConfig

    time += 1

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            if state == fire:
                state = char
            elif state == tree:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == fire:
                            state = fire
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

"""import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])"""

def count_prop(config):
    p_tree,p_fire,p_char = 0,0,0
    for x in range(width):
        for y in range(height):
            if config[x,y] == tree:
                p_tree += 1
            if config[x,y] == fire:
                p_fire += 1
            if config[x,y] == char:
                p_char += 1
    return p_tree/10000,p_fire/10000,p_char/10000

store_c = []
store_t = []        
for i in range(10):
    charred = []
    time_till_stop = []
    for initProb in np.linspace(0.1,1.0,num=9):
        init()
        prev = None
        recorded = False
        while recorded == False:
            step()
            p_tree,p_fire,p_char = count_prop(config)
            if prev == p_tree and recorded == False:
                time_till_stop.append(time)
                recorded = True
            else:
                prev = p_tree
        charred.append(p_char)
    store_c.append(charred)
    store_t.append(time_till_stop)

c = np.mean(store_c,axis = 0)
t = np.mean(store_t,axis = 0)

p = np.linspace(0.1,1.0,num=9)

plt.plot(p,c)
plt.show()
            
plt.plot(p,t)
plt.show()