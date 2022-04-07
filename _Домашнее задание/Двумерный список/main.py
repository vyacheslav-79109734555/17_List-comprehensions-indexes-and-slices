n = 4
t = 4

bivariate_list = []
for i in range(1, n + 1):
    bivariate_list.append(list([i, i + t, i + 2 * t]))
print(bivariate_list)

'''
*********** или может *************
'''

a = 12
bivariate_list = [[i + j for i in range(0, a, t)] for j in range(1, n + 1)]
print(bivariate_list)
