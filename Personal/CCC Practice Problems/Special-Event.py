people = int(input())
schedules = []
available = []
some_number = 0

for i in range(people):
    schedules.append(input())

print(schedules)

for i in range(5):
    for j in range(people):
        if schedules[j][i]== 'Y':
            some_number += 1
    available.append(some_number)
    some_number = 0

max =
print(inde)

