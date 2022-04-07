n = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

q = [c for a in n for b in a for c in b]
print(q)

for a in n:
    for b in a:
        for c in b:
            print(c, end=' ')
