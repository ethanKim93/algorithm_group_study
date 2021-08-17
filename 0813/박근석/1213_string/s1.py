import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

for i in range(10):
    tc = int(input())
    p = input()
    t = input()
    M = len(p)
    N = len(t)
    count = 0
    i = 0
    j = 0
    while i < N:
        while j < M and i < N:
            if t[i] != p[j]:
                i = i - j
                j = -1
            i = i + 1
            j = j + 1
        if j == M:
            count += 1
            i = i - j + 1
            j = 0

    print('#{} {}'.format(tc, count))