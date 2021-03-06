import random


def create_array(size, num_max):
    rand_array =[]
    for i in range(0, size + 1):
        rand_array.append(random.randint(1, num_max))
    return rand_array


def merge(a, b):
    c = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c


def merge_sort(a):
    if len(a) <= 1:
        return a
    if len(a) % 2 == 0:
        s = int(len(a)/2)
    else:
        s = int((len(a) - 1) / 2)
    left, right = merge_sort(a[:s]), merge_sort(a[s:])
    return merge(left, right)


def main():
	size = int(input("Enter the size of the number array: "))
	max = int(input("Enter the maximum value of the number array: "))
	a = create_array(size, max)
	print(a)
	s = merge_sort(a)
	print(s)

main()
