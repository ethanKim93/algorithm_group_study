# 부분집합 전체 구하기
def powerset(idx):
    if idx == n:
        for index, i in enumerate(sel):
            if i:
                print(arr[index], end=' ')
        print()
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)


arr = [1, 2, 3]
n = len(arr)
sel = [0] * n

powerset(0)