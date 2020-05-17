
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd
import copy

### MFA for SIS model

p_i = 0.03 # infection probability
p_r = 0.5 # recovery probability
n = 200
p = 0.1

# pi < pr/<k>

# For erdos-renyi graph, avg node degree is (n-1)*p

def initialize():
    global g
    g = nx.erdos_renyi_graph(n,p)
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < .5 else 0

def observe():
    global g
    cla()
    nx.draw(g, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            pos = g.pos)

def update():
    global g
    next_g = copy.deepcopy(g)
    for node in list(g.nodes):
        if g.nodes[node]['state'] == 0:
            for neighbor in list(g.neighbors(node)):
                if g.nodes[neighbor]['state'] == 1:
                    if random() < p_i: 
                        next_g.nodes[node]['state'] = 1
                        break
                else:
                    continue
        else:
            next_g.nodes[node]['state'] = 0 if random() < p_r else 1
    g = next_g



import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])


### Friendship paradox

G1 = nx.erdos_renyi_graph(1000,0.04)
G2 = nx.barabasi_albert_graph(1000,20)
G3 = nx.watts_strogatz_graph(1000,40,p = 0.05)


def avg_degree(graph):
    tot_deg = 0
    for n in graph.nodes:
        tot_deg += len(list(graph.neighbors(n)))
    
    return tot_deg/len(graph.nodes)

def avg_neighbor_deg(graph):
    tot_deg = 0
    for e in graph.edges:
        tot_deg += (len(list(graph.neighbors(e[0]))) + len(list(graph.neighbors(e[1]))))
    return (tot_deg/2)/len(graph.edges)

print('Average degree for Erdos-Renyi:', avg_degree(G1))
print('Average degree for Barabasi-Albert:', avg_degree(G2))
print('Average degree for Watts-Strogatz:', avg_degree(G3))

print('Average neibor degree for Erdos-Renyi', np.mean(list(nx.algorithms.assortativity.average_neighbor_degree(G1).values())), avg_neighbor_deg(G1))
print('Average neibor degree for Barabasi-Albert', np.mean(list(nx.algorithms.assortativity.average_neighbor_degree(G2).values())), avg_neighbor_deg(G2))
print('Average neibor degree for Watts-Strogatz', np.mean(list(nx.algorithms.assortativity.average_neighbor_degree(G3).values())), avg_neighbor_deg(G3))
