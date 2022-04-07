import random

n = int(input('Кол-во чисел в списке: '))
list_before_compress = [random.randint(0, 2) for _ in range(n)]
t = list_before_compress.count(0)
list_after_compress = [list_before_compress[i] for i in range(len(list_before_compress)) if list_before_compress[i] > 0]
list_after_compress[len(list_before_compress) - t:] = [0] * t
print('Список до сжатия:', list_before_compress)
print('Все нулевые элементы в конце массива', list_after_compress)
print('Список после сжатия:', list_after_compress[:len(list_before_compress) - t])
