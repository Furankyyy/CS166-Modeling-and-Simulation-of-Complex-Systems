import numpy as np 
import matplotlib.pyplot as plt 
import math

### Excercise 2

def diffusion_reflection(p = 0.5, p_stay = 0.4, steps = 200):
    path = [0]
    x = 0
    for _ in range(steps):
        # reflection at x = -4
        if x == -4:
            if np.random.random() < p_stay:
                continue
            else:
                x = -3
        else:
            if np.random.random() < p:
                x = x + 1
            else:
                x = x - 1
        path.append(x)
    return path

# Sample paths for diffusion with reflection
sample_path_reflection = diffusion_reflection()

plt.plot(sample_path_reflection)
plt.title("Sample paths for diffusion with reflection")
plt.xlabel("Time step")
plt.ylabel("Position")
plt.show()

# Histogram for diffusion with reflection

plt.hist(sample_path_reflection)
plt.title("Histogram for diffusion with reflection")
plt.xlabel("Position")
plt.ylabel("Frequency")
plt.show()


def diffusion_block(p = 0.5, p_stay = 0.4, p_block = 0.25, steps = 200):
    path = [0]
    x = 0
    for _ in range(steps):
        # reflection at x = -4
        if x == -4:
            if np.random.random() < p_stay:
                continue
            else:
                x = -3
        elif x == 6:
            if np.random.random() < p_block:
                x = 7
            else:
                x = 5
        elif x == 7:
            if np.random.random() < p_block:
                x = 6
            else:
                x = 8
        else:
            if np.random.random() < p:
                x = x + 1
            else:
                x = x - 1
        path.append(x)
    return path

sample_path_block = diffusion_block()

plt.hist(sample_path_block,bins = 20)
plt.title("Histogram for diffusion with partial block")
plt.xlabel("Position")
plt.ylabel("Frequency")
plt.show()

### Excercise 4

def random_walk_plane(sigma2 = 0.5, steps = 20):
    coord = [0,0]
    path = [[0,0]]
    for _ in range(steps):
        new_coord = []
        direction = np.random.random() * 360
        distance = np.random.normal(0,scale = math.sqrt(sigma2))
        new_coord.append(coord[0] + distance * math.cos(direction))
        new_coord.append(coord[1] + distance * math.sin(direction))
        coord = new_coord
        path.append(new_coord)
    return path

# Plot sample path of random walk in plane
sample_path_rw = np.array(random_walk_plane(2,1600))

plt.plot(*sample_path_rw.transpose(),)
plt.title("Sample path of random walk in plane")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Plot density
endpoints = []

for _ in range(500):
    endpoints.append(random_walk_plane(1,100)[-1])

plt.scatter([p[0] for p in endpoints],[p[1] for p in endpoints])
plt.title("Density of random walk in plane")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()



### Excercise 9a
