import pandas as pd
import wikipedia
from bs4 import BeautifulSoup

# Set up Wikipedia API
wikipedia.set_lang("en")

# Fetch the page HTML
page_title = "List of nearest galaxies"
try:
    page_html = wikipedia.page(page_title).html()
except wikipedia.exceptions.PageError:
    print(f"Page '{page_title}' does not exist.")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_html, 'html.parser')

# Find the first table on the page
table = soup.find('table', {'class': 'wikitable'})

if not table:
    print("No table found on the page.")
    exit()

# Extract table data into a list of dictionaries
data = []
headers = ['#', 'Picture', 'Galaxy', 'Type',
           'Distance (Mly)', 'Distance (Mpc)', 'Magnitude (M)', 'Magnitude (m)', 'Group Membership', 'Notes', 'Diameter (ly)']

for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all(['td', 'th'])
    if len(cells) > 1:  # Avoid empty rows
        data.append({headers[i]: cells[i].text.strip()
                    for i in range(len(cells))})

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)
# Remove the last 2 rows
df = df.iloc[:-2]

# Remove any rows without a value in the 'Diameter (ly)' column
df = df[df['Diameter (ly)'] != '']
# We only need to keep the following columns: Galaxy, Distance (Mly), Diameter (ly)
df = df[['Galaxy', 'Distance (Mly)', 'Diameter (ly)']]
# Clean up the data by removing commas, deleting everything after (and including) a ' ' or '[' (only in Distance and Diameter columns)
df['Distance (Mly)'] = df['Distance (Mly)'].str.replace(
    ',', '').str.replace('~', '').str.split(' ').str[0].str.split('[').str[0]
df['Diameter (ly)'] = df['Diameter (ly)'].str.replace(',', '').str.replace(
    '~', '').str.replace('≈ ', '').str.split(' ').str[0].str.split('[').str[0]

# Convert the 'Distance (Mly)' and 'Diameter (ly)' columns to numeric values
df['Distance (Mly)'] = pd.to_numeric(df['Distance (Mly)'])
df['Diameter (ly)'] = pd.to_numeric(df['Diameter (ly)'])


# Save the DataFrame to a CSV file
csv_path = "nearest_galaxies.csv"
df.to_csv(csv_path, index=False)
print(f"Data saved to {csv_path}")
