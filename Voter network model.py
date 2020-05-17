import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pylab import *
import networkx as nx
import random as rd
import numpy as np

def initialize():
    global g
    g = nx.karate_club_graph()
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
    listener = rd.choice(list(g.nodes))
    speaker = rd.choice(list(g.neighbors(listener)))
    g.nodes[listener]['state'] = g.nodes[speaker]['state']

#import pycxsimulator
#pycxsimulator.GUI().start(func=[initialize, observe, update])


class voter_network_origin():

    def __init__(self,p = 0.5):
        self.g = nx.karate_club_graph()
        self.p = p
        self.pos = nx.spring_layout(self.g)
        for i in self.g.nodes:
            self.g.nodes[i]['state'] = 1 if random() < self.p else 0


    def update(self):
        listener = rd.choice(list(self.g.nodes))
        speaker = rd.choice(list(self.g.neighbors(listener)))
        self.g.nodes[listener]['state'] = self.g.nodes[speaker]['state']

    def check_opinion(self):
        states = list(nx.get_node_attributes(self.g,'state').values())
        if len(set(states)) == 1:
            return False
        else:
            return True



class voter_network_reverse():
    
    def __init__(self,p = 0.5):
        self.g = nx.karate_club_graph()
        self.p = p
        self.pos = nx.spring_layout(self.g)
        for i in self.g.nodes:
            self.g.nodes[i]['state'] = 1 if random() < self.p else 0

    def update(self):
        speaker = rd.choice(list(self.g.nodes))
        listener = rd.choice(list(self.g.neighbors(speaker)))
        self.g.nodes[listener]['state'] = self.g.nodes[speaker]['state']

    def check_opinion(self):
        states = list(nx.get_node_attributes(self.g,'state').values())
        if len(set(states)) == 1:
            return False
        else:
            return True



class voter_network_edge():
    
    def __init__(self,p = 0.5):
        self.g = nx.karate_club_graph()
        self.p = p
        self.pos = nx.spring_layout(self.g)
        for i in self.g.nodes:
            self.g.nodes[i]['state'] = 1 if random() < self.p else 0

    def update(self):
        edge = rd.choice(list(self.g.edges))

        speaker = rd.choice([0,1])
        if speaker == 0:
            listener = 1
        else:
            listener = 0
        self.g.nodes[edge[listener]]['state'] = self.g.nodes[edge[speaker]]['state']

    def check_opinion(self):
        states = list(nx.get_node_attributes(self.g,'state').values())
        if len(set(states)) == 1:
            return False
        else:
            return True



def sim(model, prob=0.5, iter = 100):
    results = []
    for _ in range(iter):
        count = 0
        G = model(p=prob)
        while G.check_opinion():
            G.update()
            count += 1
        results.append(count)
    return results

results1 = sim(voter_network_origin)
results2 = sim(voter_network_reverse)
results3 = sim(voter_network_edge)

print('Average steps for original model:',np.mean(results1))
print('Average steps for reverse model:',np.mean(results2))
print('Average steps for edge model:',np.mean(results3))
plt.hist(results1,bins=15,density=True,alpha=0.5,color='red',label='Original model')
plt.hist(results2,bins=15,density=True,alpha=0.5,color='yellow',label='Reverse model')
plt.hist(results3,bins=15,density=True,alpha=0.5,color='blue',label='Edge model')
plt.legend()
plt.show()


