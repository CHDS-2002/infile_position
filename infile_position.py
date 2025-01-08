import os

os.system('COLOR B')

def custom_write(file_name, strings):
    with open(file_name, 'w+') as f:
        for s in strings:
            f.write(f"{s}\n")

    string_positions = dict()

    for s in strings:
        string_positions[(i + 1, byte(s[0])] = s

    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

try:
    os.system('PAUSE')
except:
    os.system('CLS')