import matplotlib.pyplot as plt
import numpy as np

a = 10
b = 3
n = []
for g in range(0, 180):
    t = g * np.pi / 180 - np.pi/2
    n.append(int(np.round(10*(1-3/np.sqrt(a**2+(b**2-a**2)*np.sin(t)**2)))))

print(n)

# plt.hist(n, bins=range(0, 9), align='left', rwidth=0.8)
# plt.xlabel('n for En (Hubble Eccentricity)')
# plt.ylabel('Frequency')
# plt.title('Histogram of Hubble Values')
plt.figure(figsize=(10, 6))
plt.bar(range(0, 180), n, color='pink', width=1.0, edgecolor='black')
plt.title('Histogram of En across θ (0° to 180°)')
plt.xlabel('θ (degrees)')
plt.ylabel('En values')
plt.grid(axis='y', alpha=0.7, linestyle='--')

plt.show()
