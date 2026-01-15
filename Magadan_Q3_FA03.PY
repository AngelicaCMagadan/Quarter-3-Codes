import numpy as np

names = ["Me", "Lia", "Jake"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200],  # Jake
])
 
for i in range(len(names)):
    total_steps = np.sum(steps[i])
    average_steps = np.mean(steps[i])
    minimum_steps = np.min(steps[i])
    maximum_steps = np.max(steps[i])

    print(names[i], "- Total Steps:", int(total_steps), "|", "Average: ", int(average_steps), "|", "Min: ", int(minimum_steps), "|", "Max: ", int(maximum_steps))