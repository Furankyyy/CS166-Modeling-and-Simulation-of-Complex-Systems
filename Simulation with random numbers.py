import numpy as np
import matplotlib.pyplot as plt

###Exercise 8.

class coin_sim():

    def __init__(self,prob = 0.6):
        self.p = prob
        self.x = 0
        self.path = [0]

    def toss(self):
        seed = np.random.random()
        if seed < self.p:
            self.x -= 1
        else:
            self.x +=1
        self.path.append(self.x)

# Plot one sample path
random_walk = coin_sim()
for _ in range(30):
    random_walk.toss()
plt.plot(random_walk.path)
plt.title('Sample path')
plt.xlabel('Time step')
plt.ylabel('Position')
plt.show()

# 200 random walks
hist = []   
for _ in range(200):
    random_walk = coin_sim()
    for _ in range(30):
        random_walk.toss()
    hist.append(random_walk.x)

plt.hist(hist)
plt.title('Histogram of 200 random walks')
plt.xlabel('Final position')
plt.ylabel('Frequency')
plt.show()

# Sample mean and variance
print('Sample mean:', np.mean(hist))
print('Sample variance:', np.std(hist)**2)


### Excersice 9.

class Gamble():

    def __init__(self, prob = 0.5):
        self.gambler = 100
        self.house = 2000
        self.p = prob
        self.path = [[100,2000]]

    def bet(self):
        seed = np.random.random()
        if seed < self.p:
            self.gambler -= 1
            self.house += 1
        else:
            self.gambler += 1
            self.house -= 1
        self.path.append([self.gambler,self.house])
    

upper_bound = [100,1000,10000,100000,500000,1000000,2000000]


# For sample paths
for bound in upper_bound:
    G = Gamble()
    t = 0
    while G.gambler > 0 and G.gambler < 2100 and t < bound:
        G.bet()
        t += 1
    plt.plot(np.array(G.path)[:,0], label='Bound: '+ str(bound))
plt.title('Sample paths')
plt.xlabel('Duration')
plt.ylabel('Gambler\'s money')
plt.legend(loc="best",prop={'size': 8})
plt.show()

# For histogram
mean = []
variance = []
for bound in upper_bound:
    turns = []
    for _ in range(20):
        G = Gamble()
        t = 0
        while G.gambler > 0 and G.gambler < 2100 and t < bound:
            G.bet()
            t += 1
        turns.append(t)
    plt.hist(turns)
    plt.title('Histogram of upper bound %d' % bound)
    plt.xlabel('Duration of the game')
    plt.ylabel('Frequency')
    plt.show()

    mean.append([bound,np.mean(turns)])
    variance.append([bound,np.std(turns)**2])

mean = np.array(mean)
variance = np.array(variance)


plt.plot(mean[:,0],mean[:,1])
plt.title('Sample mean')
plt.xlabel('Upper bound')
plt.ylabel('Duration of the game')
plt.show()

plt.plot(variance[:,0],variance[:,1])
plt.title('Sample variance')
plt.xlabel('Upper bound')
plt.ylabel('Duration of the game')
plt.show()

plt.loglog(mean[:,0],mean[:,1])
plt.title('Log plot sample mean')
plt.xlabel('Log upper bound')
plt.ylabel('Log duration of the game')
plt.show()

plt.loglog(variance[:,0],variance[:,1])
plt.title('Log plot variance')
plt.xlabel('Log upper bound')
plt.ylabel('Log duration of the game')
plt.show()