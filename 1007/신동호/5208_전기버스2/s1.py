import sys
sys.stdin = open('sample_input.txt')

def bus(s):
    global cnt, M
    while s < M[0]:
        if not s + M[s] < M[0]:
            return cnt
        max_d = 0
        for i in range(1, M[s]+1):
            if max_d < s + i + M[s+i]:
                max_d = s + i + M[s+i]
                before = s + i
        cnt += 1
        s = before

T = int(input())

for tc in range(1, T+1):
    M = list(map(int, input().split()))
    cnt = 0
    bus(1)
    print('#{} {}'.format(tc, cnt))            
