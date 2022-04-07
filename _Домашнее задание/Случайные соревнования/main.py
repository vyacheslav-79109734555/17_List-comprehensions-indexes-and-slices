import random

x = 20  # участников в команде
team_1 = [round(random.uniform(5, 10), 2) for _ in range(x)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(x)]
winning_team = [(team_1[i] if team_1[i] > team_2[i] else team_2[i]) for i in range(x)]

print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', winning_team)
