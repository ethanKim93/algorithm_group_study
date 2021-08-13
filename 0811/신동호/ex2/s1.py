import sys
sys.stdin = open('input.txt')


T = int(input())
#비트 연산자 사용
for tc in range(1, T+1):
    numbers = list(map(int,input().split()))
    n = len(numbers)
    for i in range(1, 1<<n): # 1을 시작점으로 지정하면서 공집합인 경우 제외할 수 있음
        sub_sum = 0
        for j in range(n):
            if i & (1<<j) :
                sub_sum += numbers[j]
        if not sub_sum:
            print('#{} {}'.format(tc,1))
            break
    else:
        print('#{} {}'.format(tc,0))