import pandas as pd

# Đọc file Excel
file_path = input() # Đường dẫn đến file Excel của bạn
df = pd.read_excel(file_path)  # Đọc toàn bộ file Excel

# Giả sử cột bạn muốn đếm là cột 'English'
# Nếu cần đếm theo chỉ số cột, có thể dùng df.iloc[:, 0] để chọn cột đầu tiên
column_data = df['English'].astype(str)  # Chuyển giá trị trong cột 'A' thành chuỗi

# Hàm đếm số từ trong một chuỗi
def count_words(text):
    words = text.split()  # Tách chuỗi thành danh sách các từ
    return len(words)  # Trả về số từ

# Đếm số từ cho toàn bộ cột và tính tổng số từ
total_word_count = column_data.apply(count_words).sum()

print(f"Tổng số từ trong cột A: {total_word_count}")
