import numpy as np

names = ["Me", "Lia", "Jake"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

total_steps = np.sum(steps, axis=1)

highest_total = np.max(total_steps)
lowest_total = np.min(total_steps)

highest_index = np.argmax(total_steps)


for i in range(len(names)):
    print(names[i], "- Total Steps:", total_steps[i])

print("\nPerson with the highest total steps:", names[highest_index])
print("Highest Total Steps:", highest_total)
print("Difference between highest and lowest total:", highest_total - lowest_total)
