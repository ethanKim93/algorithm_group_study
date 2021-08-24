# 부분합 10 구하기 구현해야합니다.
arr = [2,4,6]
N = len(arr)
sel = [0] * N

def powerset(idx):
    if idx == N:
        for index, i in enumerate(sel):
            if i:
                print(arr[index], end=' ')
        print()
        return
    sel[idx] = 1
    powerset(idx+1)

    sel[idx] = 0
    powerset(idx+1)


powerset(0)
