def custom_write(file_name, strings):
    num_byte = 0
    strings_positions = {}
    file = open(file_name, 'a', encoding = 'utf-8')
    for i in range(0, len(strings)):
        file.seek(num_byte)
        file.write((strings[i])+'\n')
        num_str = i + 1
        strings_positions.update({(num_str, num_byte):strings[i]})
        num_byte = file.tell()
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)