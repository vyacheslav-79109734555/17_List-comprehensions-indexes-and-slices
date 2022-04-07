numb = [x for x in range(1, 101) if x % 10 == 0]
new_numb = numb[:]
new_numb[3] = 0

print(new_numb)
print(new_numb[:5])
print(new_numb[5:])
print(new_numb[2:5])
print(new_numb[2:8:2])
print(new_numb[::-1])

new_numb[:3] = [1, 1, 1]
print(new_numb)
new_numb[:3] = [1]
print(new_numb)
