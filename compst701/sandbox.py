l = [5, 6, 8, 9, 12, 4]


def sum(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return num_list[0] + sum(num_list[1:])

print(sum(l))