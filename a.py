import pandas as pd

# Đọc file TSV
file_path = input()  # Đường dẫn tới file TSV
df = pd.read_csv(file_path, sep='\t')  # Đọc file .tsv

# Kiểm tra tên các cột trong file TSV
print("Các cột có trong file TSV:")
print(df.columns)
