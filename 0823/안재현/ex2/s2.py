def powerset(i, j):
    if j == i:
        for i in range(j):
            if empty[i] == 1:
                print(arr[i], end='')
        print()
    else:
        empty[i] = 0
        powerset(i+1, j)
        empty[i] = 1
        powerset(i+1, j)


arr = [1, 2, 3]
empty = [0] * 3


powerset(0, 3)
