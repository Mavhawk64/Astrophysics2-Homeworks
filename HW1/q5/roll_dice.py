import os

import numpy as np
import pandas as pd

path = os.path.dirname(__file__)

# Set np random seed
np.random.seed(174)  # Fixed seed for reproducibility


g_812 = 1e7
c_812 = 9
g_1620 = 1.8e7
c_1620 = 30
g_2428 = 2.6e7
c_2428 = 62


def check_dice(R, d):
    return int(np.round((5 * np.log10(d / 10) - 13.56 - 16) / 0.44, 2)) >= R


def roll_dice(d, c):
    count = 0
    rolls = []
    for _ in range(c):
        # roll a dice between 1 and 10
        R = np.random.randint(1, 11)
        rolls.append(R)
        count += check_dice(R, d)
    return count, rolls


c1, r1 = roll_dice(g_812, c_812)
c2, r2 = roll_dice(g_1620, c_1620)
c3, r3 = roll_dice(g_2428, c_2428)

# Output (csv)

df = pd.DataFrame(
    {
        "Shell": ["8-12 Mpc", "16-20 Mpc", "24-28 Mpc"],
        "Count": [c1, c2, c3],
        "Average Roll": [np.average(r1), np.average(r2), np.average(r3)],
        "Absolute Magnitude": [
            -13.56 - 0.44 * np.average(r1),
            -13.56 - 0.44 * np.average(r2),
            -13.56 - 0.44 * np.average(r3),
        ],
        "Rolls": [r1, r2, r3],
    }
)

# print to console
print(df)

# save to csv
df.to_csv(path + "/dice_rolls.csv", index=False)
