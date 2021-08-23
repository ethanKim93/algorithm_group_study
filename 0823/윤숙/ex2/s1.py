# 부분집합의 합을 만드는 문제
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
sel = [0] * n


def sumset(idx):
    if idx == n: #초기 idx=0
        total = []
        for idx, i in enumerate(sel):
            if i:
                total.append(arr[idx])
        sum = 0
        for d in range(len(total)):
            sum += total[d]
        if sum == n:
            print(total, sum)
        return
    sel[idx] = 1  # 1 [1,0,0]  2 [1,1,0]  3 [1,1,1] 6 [1,0,1]
    sumset(idx + 1)  # sumset(1) sumset(2) sumset(3) sumset(3)
    sel[idx] = 0  #  4 [1,1,0] 5 [1,0,0] 7 [1,0,0]
    sumset(idx + 1)  # sumset(3) sumset(2) sumser(3)


sumset(0)
