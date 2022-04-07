def encoded(text, k):
    char_list = [(a[(a.index(sym) + k) % 34] if sym != ' ' else ' ') for sym in text]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя!'

code = encoded(input('Введите сообщение: ').lower(), int(input('Введите сдвиг: ')))

print('Зашифрованное сообщение: ', code)
