import os

import matplotlib.pyplot as plt
import numpy as np

dir = os.path.dirname(os.path.realpath(__file__))

# Create linspace of t (times) from 0.1 to 1000. Let's have 0.1s intervals.
t = np.linspace(0.1, 1000, 10000)
T = 1.5e10 * t ** (-1 / 2)  # K
n_gamma = 2.03e7 * T**3  # m^-3 K^-3
eta = 6.1e-10
d_E = 2.2 * 1.60218e-13  # J
m_p = 1.67e-27  # kg
m_n = 1.675e-27  # kg
m_D = 2 * m_p  # kg
k_B = 1.38e-23  # J/K
h = 6.626e-34  # J s

# fmt: off
S = 7 / (eta * n_gamma) * 1/h**3 * (2 * np.pi * m_p * m_n * k_B * T / m_D) ** (3 / 2) * np.exp(-d_E / (k_B * T))
# fmt: on

# Debugging check
print(np.min(S), np.max(S))

# Plot S vs Time
plt.figure()
plt.plot(t, S)
plt.xlabel("Time (s)")
plt.ylabel("S")
plt.title("S vs Time")
plt.savefig(os.path.join(dir, "S_vs_time.png"))
plt.clf()  # Clear figure

# Compute x
sqt_S = np.sqrt(S**2 + 16 * S + 36)
x = (sqt_S - S - 6) / 2

# Plot x vs Time
plt.figure()
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("x")
plt.title("x vs Time")
plt.savefig(os.path.join(dir, "x_vs_time.png"))
plt.clf()

# Plot x vs S
plt.figure()
plt.plot(S, x)
plt.xlabel("S")
plt.ylabel("x")
plt.title("x vs S")
plt.savefig(os.path.join(dir, "x_vs_S.png"))
plt.clf()

# Compute n_D/n_P ratio
n_D_n_P_ratio = (1 - x) / (x + 6)

# Plot n_D/n_P ratio vs Time
plt.figure()
plt.plot(t, n_D_n_P_ratio)
plt.xlabel("Time (s)")
plt.ylabel("n_D/n_P ratio")
plt.title("n_D/n_P ratio vs Time")
plt.savefig(os.path.join(dir, "n_D_n_P_ratio_vs_time.png"))
plt.clf()

# Plot n_D/n_P ratio vs k_B*T
plt.figure()
plt.plot(k_B * T, n_D_n_P_ratio)
plt.xlabel("k_B*T (J)")
plt.ylabel("n_D/n_P ratio")
plt.title("n_D/n_P ratio vs k_B*T")
plt.xscale("log")
plt.savefig(os.path.join(dir, "n_D_n_P_ratio_vs_kBT.png"))
plt.clf()

# Close all figures to free memory
plt.close("all")
