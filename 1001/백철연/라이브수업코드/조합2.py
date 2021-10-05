
def nCr(n, r, s, k):
    if k==r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1): # n-r+k 선택할 수 있는 구간의 끝
            comb[k] = i
            nCr(n, r, i+1, k+1)

N = 10
R = 3
comb = [0] * R
nCr(N, R, 0, 0)

# 문제를 해결하기 위한 수단이 아니라 , 전처리 과정에서 선택을 위해 필요한 조합
