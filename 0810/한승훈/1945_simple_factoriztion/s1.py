import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [2, 3, 5, 7, 11] # 리스트 값이 서로의 곱으로 인수분해 되지않는다.
    lst_num = [0] * 5
    for idx in range(len(lst)):
        while N > 0:
            if not N % lst[idx]: # 나누어 떨어진다.
                lst_num[idx] += 1
                N = N / lst[idx]
            else:
                break
    print('#{}'.format(tc),end =' ')
    print(*lst_num)
