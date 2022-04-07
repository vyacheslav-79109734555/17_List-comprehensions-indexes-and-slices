text = 'привет'
text_list = list(text)

part_one = text_list[:len(text_list) // 2]
part_one = part_one[::-1]

part_two = text_list[len(text_list) // 2:]
part_two = part_two[::-1]

print(part_one + part_two)
'''
**********************************************
'''
part_one = text[:len(text) // 2]
part_two = text[len(text) // 2:]

print(part_one, '*', part_two)
print(part_one[::-1] + part_two[::-1])

print(text[:4])
print(text[4:])
print(text[0])
print(text[::-1])
print(text[::-2])

a = text[:]
print(a)
