import numpy as np

# Given recession velocity data (km/s)
rv_data = np.array(
    [
        184,
        459,
        2735,
        1683,
        2845,
        1911,
        1899,
        1239,
        1056,
        37,
        1111,
        404,
        2273,
        1204,
        1204,
        2599,
        931,
        1730,
        2140,
        803,
        1054,
        704,
        628,
        2588,
        2578,
        87,
        659,
        1839,
        751,
        1452,
        1113,
        1349,
    ]
)

# Hubble's constant (km/s/Mpc)
H0 = 72

# Compute average recession velocity
v_avg = np.mean(rv_data)

# Compute standard deviation of velocities
sigma_v = np.std(rv_data, ddof=1)  # Using sample standard deviation

# Compute average inferred distance (Mpc)
d_avg = v_avg / H0

# Compute inferred distance spread (±1σ)
sigma_d = sigma_v / H0

# True distance to the cluster center (Mpc)
d_true = 16.5

# Output results
print(f"Average Recession Velocity: {v_avg:.2f} km/s")
print(f"Average Inferred Distance: {d_avg:.2f} Mpc")
print(f"Standard Deviation of Velocities: {sigma_v:.2f} km/s")
print(f"Spread in Inferred Distances: ±{sigma_d:.2f} Mpc")
