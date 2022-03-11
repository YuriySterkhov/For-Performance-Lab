with open(input(), 'r') as f:
    num = f.readlines()
for i in range(len(num) - 1):
    num[i] = num[i].replace('\n', '')
for i in range(len(num)):
    num[i] = int(num[i])
num_changeable = []
num_changeable.extend(num)
sum_of_moves = 0
list_of_sum = []
for i in range(len(num)):
    num_changeable.pop(i)
    for j in range(len(num_changeable)):
        sum_of_moves += abs(num[i] - num_changeable[j])
    list_of_sum.append(sum_of_moves)
    sum_of_moves = 0
    num_changeable = []
    num_changeable.extend(num)
print(min(list_of_sum))