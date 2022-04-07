a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))

c = []
c.extend((range(a, b + 1, 2)))

print(c)
