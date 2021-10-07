li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(n, m, k):      # n 순열의 길이 / k 결정할 위치
    if n == k:
        # if sum(p) == 10:
            print(p)
    else:
        for i in range(m):      # 주어진 숫자의 갯수만큼 반복(갯수 순열)
            if u[i] == 0:
                u[i] = 1
                p[k] = li[i]
                func(n, m, k+1)
                u[i] = 0

p = [0] * 5
u = [0] * 5
# for i in range(6):
#     func(5, 5, i)
func(5, 5, 0)