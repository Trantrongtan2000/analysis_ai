import os
import csv

# Directory to scan
directory = 'scan'

# List to store file information
file_list = []
edata=[]
# Walk through the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file == 'Thumbs.db':
            continue
        if file.endswith('.pdf'):
            # Split the filename
            name_parts = file.split('_')
            if len(name_parts) == 3 and name_parts[2].endswith('.pdf'):
             name_parts[2] = name_parts[2][:-4]  # Remove '.pdf' from the last part
             file_list.append(name_parts)
            else:
             edata.append(file)
        else:
            edata.append(file)
# Sort the file list
file_list.sort()
edata.sort()
# Write to CSV
with open('sorted_files3.csv', 'w',encoding="utf-8", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Thiết bị', 'Khoa phòng', 'Đề xuất/ Số hợp đồng'])
    csvwriter.writerows(file_list)
    for error in edata:
        csvwriter.writerow([error, '', ''])
print("Các tên bị lỗi: ")
print(edata)
# Calculate the ratio of edata files to file_list files
if file_list:
    ratio = len(edata) / len(file_list)
else:
    ratio = float('inf')  # Avoid division by zero if file_list is empty

print(f"\n Tỉ lệ file lỗi trên dữ liệu scan: {(ratio)*100:.2f}")