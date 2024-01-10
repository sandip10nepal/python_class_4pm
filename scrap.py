from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
url = 'https://www.sharesansar.com/live-trading'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

if table:
    rows = table.find_all('tr')
    
    # Create an empty list to store all rows
    all_rows = []

    for row in rows:
        columns = row.find_all(['th', 'td'])
        rowData = [col.text.strip() for col in columns]
        
        # Append each row's data to the overall list
        all_rows.append(rowData)

# Open the CSV file in append mode
with open('nepse.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)    
    # Write all rows to the CSV file
    csv_writer.writerows(all_rows)
    
df = pd.read_csv('nepse.csv')
print(df)