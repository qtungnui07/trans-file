import sys
import pandas as pd
import io
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

genai.configure(api_key="AIzaSyCIpuQaqEffYBLgKFuj8cy3JakRUotgQyI")

generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)


file_path = input()
read = pd.read_excel(file_path)


translated_texts = []

for text in read['English']:
    prompt = f"Translate the following English text to Vietnamese: '{text}'"
    response = model.generate_content(
    prompt,
    safety_settings={
        'HATE': 'BLOCK_NONE',
        'HARASSMENT': 'BLOCK_NONE',
        'SEXUAL' : 'BLOCK_NONE',
        'DANGEROUS' : 'BLOCK_NONE'
    })
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    translated_texts.append(response.text)

txt_file_path = file_path.replace('.xlsx', '_translated.txt')

with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
    for original, translated in zip(read['English'], translated_texts):
        txt_file.write(f"Original: {original}\nTranslated: {translated}\n\n")

print(f"Đã lưu bản dịch tại: {txt_file_path}")