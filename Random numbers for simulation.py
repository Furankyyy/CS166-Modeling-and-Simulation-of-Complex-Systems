import scipy as sp
import numpy as np 
import matplotlib.pyplot as plt

### Exercise 14
lmd = [0.1,0.5,1,1.5,2,3,4,5,6,7,8,10]
beta = [1/x for x in lmd]

time_lmd = []
mean_wait = []

for b in beta:
    buses = sp.random.exponential(b,size=10)
    tot_time = sum(buses)
    passenger_arrive = sp.random.uniform(0,tot_time,size=10)
    time_stamp = sp.cumsum(buses)
    wait_time = []
    for arrival in passenger_arrive:
        bus_come = time_stamp[time_stamp.searchsorted(arrival)]
        time_lmd.append([bus_come - arrival,1/b])
        wait_time.append(bus_come - arrival)
    mean_wait.append([np.mean(wait_time),1/b])

time_lmd = np.array(time_lmd)  
mean_wait = np.array(mean_wait)

plt.scatter(time_lmd[:,1],time_lmd[:,0])
plt.plot(mean_wait[:,1],mean_wait[:,0],color='orange',label='Mean waiting time')
plt.title('Lambda values and waiting time')
plt.xlabel('Lambda')
plt.ylabel('Passenger waiting time')
plt.legend()
plt.show()




time_lmd = []
mean_wait = []

for b in beta:
    buses = sp.random.uniform(0,2/b,size=10)
    tot_time = sum(buses)
    passenger_arrive = sp.random.uniform(0,tot_time,size=10)
    time_stamp = sp.cumsum(buses)
    wait_time = []
    for arrival in passenger_arrive:
        bus_come = time_stamp[time_stamp.searchsorted(arrival)]
        time_lmd.append([bus_come - arrival,1/b])
        wait_time.append(bus_come - arrival)
    mean_wait.append([np.mean(wait_time),1/b])

time_lmd = np.array(time_lmd)  
mean_wait = np.array(mean_wait)

plt.scatter(time_lmd[:,1],time_lmd[:,0])
plt.plot(mean_wait[:,1],mean_wait[:,0],color='orange',label='Mean waiting time')
plt.title('Lambda values and waiting time')
plt.xlabel('Lambda')
plt.ylabel('Passenger waiting time')
plt.legend()
plt.show()


### Excercise 24

data = {
    50: 0.00832,
    51: 0.00911,
    52: 0.00996,
    53: 0.01089,
    54: 0.01190,
    55: 0.01300,
    56: 0.01421,
    57: 0.01554,
    58: 0.01700,
    59: 0.01859,
    60: 0.02034,
    61: 0.02224,
    62: 0.02431,
    63: 0.02657,
    64: 0.02904,
    65: 0.03175,
    66: 0.03474,
    67: 0.03804,
    68: 0.04168,
    69: 0.04561,
    70: 0.04979,
    71: 0.05415,
    72: 0.05865,
    73: 0.06326,
    74: 0.06812,
    75: 0.07337,
    76: 0.07918,
    77: 0.08570,
    78: 0.09306,
    79: 0.10119,
    80: 0.10998,
    81: 0.11935,
    82: 0.12917,
    83: 0.13938,
    84: 0.15001,
    85: 0.16114,
    86: 0.17282,
    87: 0.18513,
    88: 0.19825,
    89: 0.21246,
    90: 0.22814,
    91: 0.24577,
    92: 0.26593,
    93: 0.28930,
    94: 0.31666,
    95: 0.35124,
    96: 0.40056,
    97: 0.48842,
    98: 0.66815,
    99: 0.72000,
    100: 0.76000,
    101: 0.80000,
    102: 0.85000,
    103: 0.90000,
    104: 0.96000,
    105: 1.00000}


money_remain = []
death = []

for _ in range(1000):
    money = 150000
    age = 50
    p = np.random.random()
    while p > data[age]:
        money = money * (1 + sp.random.normal(0.08,0.09))
        if age <= 70:
            money += 10000
        else:
            money -= 65000
        age += 1
        p = np.random.random()
    money_remain.append(money)
    death.append(age)

print(np.mean(money_remain))

plt.scatter(death,money_remain)
plt.title('Age dead and money remain')
plt.xlabel('Age dead')
plt.ylabel('Money remain')
plt.show()