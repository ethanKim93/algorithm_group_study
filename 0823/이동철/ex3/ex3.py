arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N


def powerset(idx, subsum):
    if subsum > 10:
        return
    if idx == N:
        if subsum == 10:
            for index, i in enumerate(sel):
                if i:
                    print(arr[index], end=' ')
            print()
            return
    else:
        sel[idx] = 1
        powerset(idx+1, subsum + arr[idx])
        sel[idx] = 0
        powerset(idx+1, subsum)


powerset(0, 0)