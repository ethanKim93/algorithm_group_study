import sys
sys.stdin = open('sample_input.txt')

def search(n):
    global ans
    start = 0
    end = N - 1
    dir = ''
    while start <= end:
        mid = (start+end)//2
        if sort_lst[mid] < n:
            start = mid+1
            if dir == 'r':
                return
            dir = 'r'
        elif sort_lst[mid] > n:
            end = mid-1
            if dir == 'l':
                return
            dir = 'l'
        else:
            ans += 1
            return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    sort_lst = sorted(list(map(int, input().split())))
    random_lst = list(map(int, input().split()))
    ans = 0
    for num in random_lst:
        search(num)
    print('#{} {}'.format(tc, ans))