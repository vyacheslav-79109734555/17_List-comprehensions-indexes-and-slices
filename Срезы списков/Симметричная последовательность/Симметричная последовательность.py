def is_palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return True
    else:
        return False


num = [1, 2, 3, 4, 5]
answer = []

for i_num in range(0, len(num)):
    if is_palindrome(num[i_num:len(num)]):
        answer = num[:i_num]
        answer.reverse()
        break
print('Исходный список:', num)
print('Нужно чисел для палиндрома:', len(answer))
print('Список чисел:', answer)

num.extend(answer)
print(num)
