import random

teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
offices = [[], [], []]

for teacher in teachers:
    office = random.randint(0, 2)
    offices[office].append(teacher)

print(offices)
