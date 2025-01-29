import numpy as np


g_812 = 1e7
c_812 = 9
g_1620 = 1.8e7
c_1620 = 30
g_2428 = 2.6e7
c_2428 = 62


def check_dice(R, d):
    return int(np.round((5 * np.log10(d/10) - 13.56 - 16) / 0.44, 2)) >= R


def roll_dice(d, c):
    count = 0
    for _ in range(c):
        # roll a dice between 1 and 10
        R = np.random.randint(1, 11)
        count += check_dice(R, d)
    return count


print(roll_dice(g_812, c_812))
print(roll_dice(g_1620, c_1620))
print(roll_dice(g_2428, c_2428))
