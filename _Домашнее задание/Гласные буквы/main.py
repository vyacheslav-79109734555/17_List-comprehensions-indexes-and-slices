text = list(input('Введите текст: '))
vowel_letters = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowel_letters_list = []

for i_text in range(len(text)):
    for i_tex in range(len(vowel_letters)):
        if text[i_text] == vowel_letters[i_tex]:
            a = text[i_text]
            vowel_letters_list.append(a)
print('Список гласных букв:', vowel_letters_list)
print('Длина списка:', len(vowel_letters_list))

'''
********************************
'''

text = input('Введите текст: ')
vowel_letters = 'аиеёоуыэюя'
x = [i for i in text if i in vowel_letters]

print('Список гласных букв:', x)
print('Длина списка:', len(x))
