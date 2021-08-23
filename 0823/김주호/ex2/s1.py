arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
check = [0] * N


def powerset(li, tf, num=0, total=0):
    if total > 10 or total + sum(li[num:]) < 10:
        return

    if num == len(li) and total == 10:
        for i in range(len(li)):
            if tf[i]:
                print(li[i], end=" ")
        print()
        return

    tf[num] = 1
    total += arr[num]
    powerset(li, tf, num + 1, total)
    tf[num] = 0
    total -= arr[num]
    powerset(li, tf, num + 1, total)


powerset(arr, check)
