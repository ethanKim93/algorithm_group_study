arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
check = [0] * n

def powerset(idx, sum_num):
    if sum_num > 10:
        return
    if idx == n:
        if sum_num == 10:
            for i in range(idx):
                if check[i]:
                    print(arr[i], end=" ")
            print()
        return
    else:
        check[idx] = 1
        powerset(idx + 1, sum_num + arr[idx])
        check[idx] = 0
        powerset(idx + 1, sum_num)

powerset(0, 0)
