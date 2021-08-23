# 합이 10인 부분집합 구하기
def powerset(idx):
    if idx == n:
        total = 0
        ten = []
        for index, i in enumerate(sel):
            if i:
                total += arr[index]
                ten.append(arr[index])
        if total == 10:
            print(ten)
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)


arr = range(1, 11)
n = len(arr)
sel = [0] * n

powerset(0)