import random

n = int(input('Введите длину списка: '))
n_list = random.randint(0, n)
result = []
x = [(1 if i_n % 2 == 0 else i_n % 5) for i_n in range(n)]
print('Результат:', x)
