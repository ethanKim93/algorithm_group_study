import sys

sys.stdin = open('sample_input.txt')

Test = int(input())

for tc in range(Test):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))

    ans = 0
    switch = [0]*len(W)
    for i in range(M):
        full_W = 0
        last = 101
        for j in range(N):
            if T[i] >= W[j] >= full_W and switch[j] == 0:
                if last != 101:
                    switch[last] = 0
                last = j
                switch[j] = 1
                full_W = W[j]
        ans += full_W

    print("#{} {}".format(tc + 1, ans))
