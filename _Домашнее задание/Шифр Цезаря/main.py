'''
http://kodesource.top/python-exercises/string/python-data-type-string-exercise-25.php
'''


def encoded(text, k):
    in_text = []
    crypt_text = []

    a = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И',
         'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
         'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
         'Э', 'Ю', 'Я']
    b = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
         'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
         'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
         'э', 'ю', 'я']

    for letter in text:
        if letter in a:
            index = a.index(letter)
            crypto_protection = (index + k) % 33
            crypt_text.append(crypto_protection)
            new_letter = a[crypto_protection]
            in_text.append(new_letter)
        elif letter in b:
            index = b.index(letter)
            crypto_protection = (index + k) % 33
            crypt_text.append(crypto_protection)
            new_letter = b[crypto_protection]
            in_text.append(new_letter)
        elif letter in ' ':
            in_text.append(letter)

    return in_text, crypt_text


code = encoded(input('Введите сообщение: '), int(input('Введите сдвиг: ')))

print('Зашифрованное сообщение:', *code[0])
print('Цифровое значение зашифрованного сообщения:\n', code[1])
