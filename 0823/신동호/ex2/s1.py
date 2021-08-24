arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
# subsum = 0
tot = 10

def powerset(idx):
    if idx == N:
        for idx, i in enumerate(sel):
            if i:
                print(arr[idx], end = ' ')
        print()
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)

# powerset(0)

def sum_check(idx, subsum):
    if subsum == tot:
        for idx, i in enumerate(sel):
            if i:
                print(arr[idx], end = ' ')
        print()
        return
    if idx == N:
        return
    if subsum + arr[idx] <= tot:
        sel[idx] = 1
        sum_check(idx+1, subsum + arr[idx])
    sel[idx] = 0
    sum_check(idx+1, subsum)

sum_check(0, 0)