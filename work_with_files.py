with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

with open('data.txt', 'a', encoding='utf-8') as file:
    content = input('Введите текст: ')
    file.write(content)

with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())

with open('data.txt', 'rb') as sourse_file:
    data = sourse_file.read()

with open ('data_copy.txt', 'wb') as destination_file:
    destination_file.write(data)

