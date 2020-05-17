
import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

g = nx.erdos_renyi_graph(30, 0.05, directed=True, seed=123)
#nx.draw(g, pos=nx.kamada_kawai_layout(g))

class random_surfer():

    def __init__(self, G):
        self.G = G

    def surf(self, alpha, iter = 10000):
        self.alpha = alpha
        self.result = {}

        current_node = random.choice(list(self.G.nodes()))

        for _ in range(iter):
            neighbor = self.G[current_node]

            seed = random.random()

            if seed < self.alpha:

                # If meet dead end (dangling nodes), restart.
                if len(list(neighbor.keys())) == 0:
                    next_node = random.choice(list(self.G.nodes()))
                else:
                    next_node =  random.choice(list(neighbor.keys()))

            else:

                next_node = random.choice(list(self.G.nodes()))

            if next_node in self.result.keys():
                self.result[next_node] += 1
            else:
                self.result[next_node] = 1

            current_node = next_node

        return self.result



def normalize(walks):
    # Normalize each result in a list of walks.
    for w in walks:
        normalize = np.sum(list(w.values()))
        for key, value in w.items():    
            w[key] = value/normalize


walks = []
iters = np.arange(100,5000,100)

for N in iters:
    surfer_model = random_surfer(g)
    walks.append(surfer_model.surf(alpha = 0.85, iter = N))

pagerank = nx.pagerank(g)
normalize(walks)


average_abs_diff = []
for w in walks:
    error = 0
    for key in pagerank.keys():
        if key in w.keys():
            error += abs(pagerank[key] - w[key])
        else:
            error += abs(pagerank[key])
    error = error/len(pagerank.keys())
    average_abs_diff.append(error)


plt.plot(iters,average_abs_diff)
plt.xlabel('Number of steps')
plt.ylabel('Mean absolute difference between random walk results and Pagerank')
plt.show()

