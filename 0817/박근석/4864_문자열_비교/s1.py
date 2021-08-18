import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def BruteForce(p, t):
    i = 0
    j = 0
    while i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return 1
    else: return 0


for tc in range(1, T+1):
    p = input()
    t = input()
    M = len(p)
    N = len(t)

    print('#{} {}'.format(tc, BruteForce(p, t)))