people = int(input())
schedules = []
available = []
some_number = 0

for i in range(people):
    schedules.append(input().split())

print(schedules)

for i in range(5):
    for j in range(people):
        if schedules[j][i] == 'Y':
            some_number += 1

