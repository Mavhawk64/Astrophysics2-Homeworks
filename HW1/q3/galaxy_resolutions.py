import pandas as pd
from numpy import arctan

# Load the data from the CSV file nearest_galaxies.csv
df = pd.read_csv("nearest_galaxies.csv")
# Galaxy, Distance (Mly), Diameter (ly)
# Convert Distance to ly
df['Distance (ly)'] = df['Distance (Mly)'] * 1e6

R = 3.66e-3  # Resolution of the telescope in radians
galaxy_list = []
for i, row in df.iterrows():
    # Calculate the angular size of the galaxy in radians
    angular_size = 2 * \
        arctan(row['Diameter (ly)'] / (2 * row['Distance (ly)']))
    # Calculate the number of pixels needed to resolve the galaxy
    pixels = angular_size / R
    galaxy_list.append({'Galaxy': row['Galaxy'], 'Pixels': pixels})

for i in galaxy_list:
    if i["Pixels"] > 1:
        print(f"{i['Galaxy']} requires {int(i['Pixels'])} pixel(s) to resolve.")

print([i['Galaxy'] for i in galaxy_list if i['Pixels'] > 1])
