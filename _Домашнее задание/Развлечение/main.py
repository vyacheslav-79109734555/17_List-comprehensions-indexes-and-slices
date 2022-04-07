stick = int(input('Кол-во палок: '))
cast = int(input('Кол-во бросков: '))

list_I = ['I' for i in range(stick)]
print(list_I)

for i in range(1, cast + 1):
    for j in range(int(input(f'Бросок {i} Сбиты палки с номера: ')) - 1, int(input('по номер: '))):
        list_I[j] = '.'
print('Результат:', ' '.join(list_I))
