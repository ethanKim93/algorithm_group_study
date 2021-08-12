import sys
sys.stdin = open('input.txt')

T = int(input())
#카운팅 정렬
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    sort = [0] * 50 #숫자가 50이하
    for number in numbers:
        sort[number] += 1

    print('#{}'.format(tc), end=' ')
    for ind in range(len(sort)):
        while sort[ind]:
            print(ind, end=' ')
            sort[ind] -= 1
    print()