# Медленный код
# num_squares = []
# for x in range(10):
#     num_squares.append(x ** 2)
# print(num_squares)

# **********************************

list_number_in_squares = [x ** 2 for x in range(1, 6)]
print('Число в квадрате от 1 до 6:', list_number_in_squares)

list_number_in_squares = [x ** 2 for x in range(1, 6) if x % 2 != 0]
print('Не четное число в квадрате:', list_number_in_squares)

list_number_in_squares = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(1, 6)]
print('Не четное число в квадрате, а четные в кубе:', list_number_in_squares)
