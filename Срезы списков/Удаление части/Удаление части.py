import random

n = [random.randint(1, 10) for _ in range(10)]
print(n)

numb_1 = [random.randint(1, 3) for _ in range(1)]
numb_2 = [random.randint(4, 6) for _ in range(1)]

for i in numb_1:
    print(i)
for w in numb_2:
    print(w)

new_n = n[:]

s = new_n[:i]
s.extend(new_n[w:])
print('s', s)
