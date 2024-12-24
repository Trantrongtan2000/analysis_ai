import os
import csv

# Get the list of all files and directories
path = input('Nhap ten thu muc: ')
path= 'scan'
#dir_list = os.listdir(path)


print("Files and directories in '", path, "' :")
# prints all files
def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths

def extract_file_info(file_name):
  try:
    name= file_name.replace(".pdf","")
    parts = name.split("_")
    if len(parts) >= 2 and len(parts) <= 3:
      return parts
    elif len(parts) > 3:
      #print('lon hon 3')
      #print(parts)
      parts[2]=str(parts[2])+'_'+str(parts[3])
      #print('test')
      #print(parts)
      return parts
    else:
      edata.append(file_name)
      return [] # Return an empty list instead of None
  except:
    return [] # Return an empty list instead of None

output_dir = input("Nhap ten thu muc: ")
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

output_file = os.path.join(output_dir, "list_files.csv")
data=[]
edata=[]
#print(dir_list)
full_file_paths = get_filepaths(path)

for i in full_file_paths:
    t=i.split('\\')
    a=extract_file_info(t[1])
    print(t)
    #create_csv_file(output_file, a)
    data.append(a)
    print(a)

def create_csv_file(output_file, data):
  """
  Hàm tạo file CSV từ dữ liệu

  Args:
    output_file: Đường dẫn đến file CSV
    data: Danh sách các tuple chứa dữ liệu cho mỗi hàng
  """
  with open(output_file, 'w',encoding="utf-8") as csvfile:
    fieldnames = ['Thiết bị', 'Khoa phòng', 'Đề xuất/ Số hợp đồng']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)  # Viết header
    # Filter out empty lists before writing to the CSV
    for row in data:
        if row:  # Check if the row is not empty
            writer.writerow(row)  # Viết dữ liệu

#print(data)
create_csv_file(output_file, data)
#create_csv_file(output_file, edata)
print("Các tên bị lỗi: ")
print(edata)