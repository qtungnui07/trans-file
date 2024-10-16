from openai import OpenAI
import pandas as pd
import os

client = OpenAI(api_key="")

checkpoint_file = "checkpoint.txt"

def read_checkpoint():
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, "r") as f:
            content = f.read().strip()
            if content.isdigit():
                return int(content)
    return 0

def write_checkpoint(row_num):
    with open(checkpoint_file, "w") as f:
        f.write(str(row_num))

def translate_text(text, source_lang='en', target_lang='vi'):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a helpful translator from {source_lang} to {target_lang}."},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        translated_text = response.choices[0].message.content.strip()
        print(f"Đã dịch: {translated_text}")  # In ra đoạn văn bản đã dịch để kiểm tra
        return translated_text
    except Exception as e:
        print(f"Lỗi khi dịch: {e}")
        return text

def translate_column(input_file, output_file):
    df = pd.read_excel(input_file)

    # Kiểm tra nếu cột English có dữ liệu
    print("Cột English có dữ liệu:", df['English'].head())

    if 'English' not in df.columns:
        raise ValueError("Cột 'English' không tồn tại trong file.")

    start_row = read_checkpoint()

    if len(df) == 0:
        print("Không có dữ liệu trong file Excel.")
        return

    with open(output_file, "a", encoding="utf-8") as f:
        for i in range(start_row, len(df)):
            text = str(df.loc[i, 'English'])
            if not text:
                print(f"Dòng {i + 1} rỗng, bỏ qua.")
                continue

            print(f"Đang dịch dòng {i + 1}: {text}")
            translated_text = translate_text(text)
            f.write(f"\n{translated_text}\n\n")
            f.flush()
            write_checkpoint(i + 1)

    print(f"Đã lưu file đã dịch tại: {output_file}")

# Đường dẫn tới file Excel đầu vào và tệp văn bản đầu ra
input_file = 'input.xlsx'
output_file = 'translated_output.txt'

translate_column(input_file, output_file)
