import numpy as np

names = ["Me", "Lia", "Jake"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
])

for i in range(len(names)):
    print(names[i], steps[i])

print("Jake's steps on Wednesday:", steps[2, 2])

print("My steps:", steps[0])

print("Updating my Thursday steps to 5500.")
steps[0, 3] = 5500

print("My updated steps:", steps[0])