import sys
sys.stdin = open('sample_input.txt')

def check(b):
    global cnt, A
    l = 0
    r = N-1
    flag = 0
    while l <= r:
        m = (l+r)//2
        if A[m] == b:
            cnt += 1
            return
        elif A[m] > b:
            if flag == 'L':
                return
            r = m-1
            flag = 'L'
        else:
            if flag == 'R':
                return
            l = m+1
            flag = 'R'


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int ,input().split()))) # 이거 진짜 억울한데 당연히 A 정렬된 상태로 주는 줄 알았다가 정렬 안 된 A가 테스트 케이스에 섞여있어서 거의 1시간 날렸습니다
    B = list(map(int ,input().split()))
    cnt = 0
    for b in B:
        check(b)
    print('#{} {}'.format(tc, cnt))