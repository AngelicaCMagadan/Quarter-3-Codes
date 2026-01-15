import numpy as np

names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

daily_totals = np.sum(steps, axis=0)

for i in range(len(days)):
    print(days[i], "- Total Steps:", daily_totals[i])

most_active_index = np.argmax(daily_totals)

print("\nMost active day overall:", days[most_active_index])
print("Steps on that day:", daily_totals[most_active_index])
