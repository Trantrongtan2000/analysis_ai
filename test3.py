import os
import csv


# Directory containing the files
directory = 'scan'

# List to store the parsed data
data = []

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):  # Assuming the files are .txt, change if necessary
        parts = filename.split('_')
        if len(parts) == 3:
            ten_thiet_bi, khoa, so_de_xuat = parts
            data.append([ten_thiet_bi, khoa, so_de_xuat])

# Write the data to a CSV file
csv_file = 'output.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tên thiết bị', 'Khoa', 'Số đề xuất'])
    writer.writerows(data)