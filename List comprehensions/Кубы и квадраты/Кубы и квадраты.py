a = int(input('Введите число Левая граница списка: '))
b = int(input('Введите число Правая граница списка: '))

list_cubes_num = [x ** 3 for x in range(a, b + 1)]
print(list_cubes_num)

list_squares_num = [x ** 2 for x in range(a, b + 1)]
print(list_squares_num)
