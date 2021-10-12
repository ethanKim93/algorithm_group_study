import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    n1 = sorted(list(map(int, input().split())))
    n2 = list(map(int, input().split()))

    result = 0
    for num in n2:
        way = 0
        ans = -1
        L, R = 0, N-1
        while ans != num:
            C = (L + R) // 2
            if L >= R and num != n1[C]:
                break

            if num == n1[C]:
                ans = n1[C]
                result += 1

            if num > n1[C]:
                L = C+1
                if way == 'right':
                    break
                else:
                    way = 'right'
            elif num < n1[C]:
                R = C-1
                if way == 'left':
                    break
                else:
                    way = 'left'

    print('#{} {}'.format(tc, result))




