import random

num_list = []
for i in range(0, 10001):
    num_list.append(random.randint(0, 100000))


num_list.sort()
print(num_list)