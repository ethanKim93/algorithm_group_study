def powerset(i, j):
    result = 0
    empty_lst = []
    global cnt
    if j == i:
        for i in range(j):
            if empty[i] == 1:
                result += arr[i]
                empty_lst.append(arr[i])
        if result == 10:
            cnt += 1
            print('#{}'.format(cnt), end='')
            for k in range(len(empty_lst)):
                print(' {}'.format(empty_lst[k]), end='')
            print()
    else:
        empty[i] = 0
        powerset(i+1, j)
        empty[i] = 1
        powerset(i+1, j)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
empty = [0] * len(arr)
cnt = 0

powerset(0, len(arr))
