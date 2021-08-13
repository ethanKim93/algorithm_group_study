import sys
sys.stdin=open('test_input.txt', 'rt', encoding='UTF-8')

for _ in range(10):
    T = int(input())
    p = input()
    t = input()

    m = len(p)
    n = len(t)

    i = 0       # t의 인덱스
    j = 0       # p의 인덱스
    cnt = 0     # 패턴 발견 횟수
    while i < n:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == m:
            cnt += 1
            j = 0

    print('#{} {}'.format(T, cnt))