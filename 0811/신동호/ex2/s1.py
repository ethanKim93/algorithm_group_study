import sys
sys.stdin = open('input.txt')


T = int(input())
#비트 연산자 사용
for tc in range(1, T+1):
    numbers = list(map(int,input().split()))
    n = len(numbers)
    for i in range(1<<n):
        sub = []
        for j in range(n):
            if i & (1<<j) :
                sub.append(numbers[j])
        if len(sub) and (sum(sub) == 0):
            print('#{} {}'.format(tc,1))
            break
    else:
        print('#{} {}'.format(tc,0))