import re

def match_lowercase_letters():
    file_path = file_path = r'D:\MEmu\row (3).txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(data)
    return matches

print("Task:", match_lowercase_letters())
