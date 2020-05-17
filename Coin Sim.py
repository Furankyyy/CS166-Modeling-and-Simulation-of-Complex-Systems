import numpy as np
import matplotlib.pyplot as plt 
import math

class coin_sim():

    def __init__(self,p = 0.6, money = 250):
        self.result = []
        self.p = p
        self.money = money


    def flip(self, n = 1000):
        for _ in range(1000):
            if self.money <= 1:
                break
            else:
                bet = math.ceil(0.2 * self.money)
                if np.random.random() < self.p:
                    self.money += bet
                else:
                    self.money -= bet
                self.result.append(self.money)
        return self.result

cs = coin_sim()
res = cs.flip()
print(res)

#print(res)
plt.plot(res)
plt.xlabel('Time step')
plt.ylabel('Total money')
plt.show()

