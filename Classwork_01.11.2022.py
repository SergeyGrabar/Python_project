# students = ['Ivan', 'Denis', 'Kateryna', 'Vitalii']
# students.pop(1)
# print(students)

import random

stats = []
attributes = 5

print('Stats: ', end='')
for i in range(attributes):
    r = random.randint(40, 70)
    stats.append(r)
    print(stats[i], end=' ')

print('''
   [1] - Sila
   [2] - Lovk
   [3] - Intelekt
   [4] - Mudr
   [5] - Harisma''')
select = int(input('Select: '))
select -= 1
stats[select] = stats[select] + random.randint(5, 10)

for i in range(len(stats)):
    if i == select:
        continue
    stats[i] = stats[i] - random.randint(5, 10)
print('Stats: ', end='')
for i in range(attributes):
    print(stats[i], end=' ')


