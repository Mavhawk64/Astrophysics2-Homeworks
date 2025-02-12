import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# RV data
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

# Compute mean and standard deviation (Gaussian fit)
mu, sigma = np.mean(rv_data), np.std(rv_data, ddof=1)  # Sample std deviation

# Create histogram
plt.figure(figsize=(10, 6))
count, bins, _ = plt.hist(
    rv_data, bins=6, density=True, edgecolor="black", alpha=0.7, label="Histogram"
)

# Generate Gaussian curve
x = np.linspace(min(rv_data), max(rv_data), 1000)  # Smooth x range
gaussian_curve = norm.pdf(x, mu, sigma)  # Gaussian distribution

# Plot Gaussian curve on histogram
plt.plot(
    x, gaussian_curve, "r-", lw=2, label=f"Gaussian Fit\nμ={mu:.2f}, σ={sigma:.2f}"
)

# Labels and title
plt.xlabel("Recession Velocity (km/s)")
plt.ylabel("Normalized Frequency")
plt.title("Histogram of Recession Velocity Data (Gaussian Fit)")
plt.legend()

# Show grid
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save the figure in the same directory as the script
output_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "Figure_1_Gaussian.png"
)
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show plot
plt.show()

print(f"Histogram with Gaussian fit saved at: {output_path}")
