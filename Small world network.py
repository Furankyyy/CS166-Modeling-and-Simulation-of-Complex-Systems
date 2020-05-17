import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd
import numpy as np



n = 36 # number of nodes
k = 4 # number of neighbors of each node

def initialize():
    global g
    g = nx.Graph()
    length = int(np.sqrt(n))
    for i in range(1,length+1):
        for j in range(1,length+1):
            if (j != 1 and j != length) and (i != 1 and i != length):
                g.add_edge(i*j-1, (i+1)*j-1)
                g.add_edge(i*j-1, (i-1)*j-1)
                g.add_edge(i*j-1, i*(j+1)-1)
                g.add_edge(i*j-1, i*(j-1)-1)
            if (j == 1) and (i != 1 and i != length):
                g.add_edge(i*j-1, (i+1)*j-1)
                g.add_edge(i*j-1, (i-1)*j-1)
                g.add_edge(i*j-1, i*(j+1)-1)
            if (j == length) and (i != 1 and i != length):
                g.add_edge(i*j-1, (i+1)*j-1)
                g.add_edge(i*j-1, (i-1)*j-1)
                g.add_edge(i*j-1, i*(j-1)-1)
            if (i == 1) and (j != 1 and j != length):
                g.add_edge(i*j-1, i*(j+1)-1)
                g.add_edge(i*j-1, i*(j-1)-1)
                g.add_edge(i*j-1, (i+1)*j-1)
            if (i == length) and (j != 1 and j != length):
                g.add_edge(i*j-1, i*(j+1)-1)
                g.add_edge(i*j-1, i*(j-1)-1)
                g.add_edge(i*j-1, (i-1)*j-1)
            if (j == 1) and (i == 1):
                g.add_edge(i*j-1, i*(j+1)-1)
                g.add_edge(i*j-1, (i+1)*j-1)
            if (j == 1) and (i == length):
                g.add_edge(i*j-1, i*(j+1)-1)
                g.add_edge(i*j-1, (i-1)*j-1)
            if (j == length) and (i == 1):
                g.add_edge(i*j-1, i*(j-1)-1)
                g.add_edge(i*j-1, (i+1)*j-1)
            if (j == length) and (i == length):
                g.add_edge(i*j-1, i*(j-1)-1)
                g.add_edge(i*j-1, (i-1)*j-1)



    g.pos = nx.spring_layout(g)
    g.count = 0

def observe():
    global g
    cla()
    nx.draw(g, pos = g.pos)

def update():
    global g
    g.count += 1
    if g.count % 20 == 0: # rewiring once in every 20 steps
        nds = list(g.nodes)
        i = rd.choice(nds)
        if g.degree[i] > 0:
            g.remove_edge(i, rd.choice(list(g.neighbors(i))))
            nds.remove(i)
            for j in g.neighbors(i):
                nds.remove(j)
            g.add_edge(i, rd.choice(nds))

    # simulation of node movement
    g.pos = nx.spring_layout(g, pos = g.pos, iterations = 5)



import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])




for m in [1,3,5]:
    m0 = 5 # number of nodes in initial condition

    def initialize():
        global g
    g = nx.complete_graph(m0)
    g.pos = nx.spring_layout(g)
    g.count = 0

    def observe():
        global g
        cla()
        nx.draw(g, pos = g.pos)

    def pref_select(nds):
        global g   
        r = uniform(0, sum(g.degree(i) for i in nds)) 
        x=0
        for i in nds:
            x += g.degree(i)
            if r <= x:
                return i

    def update():
        global g
        g.count += 1
        if g.count % 20 == 0: # network growth once in every 20 steps 
            nds = list(g.nodes)
            newcomer = max(nds) + 1
            for i in range(m):
                j = pref_select(nds)
                g.add_edge(newcomer, j)
                nds.remove(j)
            g.pos[newcomer] = (0, 0)
            # simulation of node movement
        g.pos = nx.spring_layout(g, pos = g.pos, iterations = 5)
    
    pycxsimulator.GUI().start(func=[initialize, observe, update])