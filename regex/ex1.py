import re

file_path = file_path = r'D:\MEmu\row (3).txt'

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

pattern = 'ab*'

matches = re.findall(pattern, data)
for match in matches:
    print(match)
