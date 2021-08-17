import sys
sys.stdin = open("sample_input.txt")


def check(target, left, right):
    while left < right:
        if target[left] == target[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    li = [list(input()) for _ in range(N)]
    li_rev = [list(li[i][j] for i in range(N)) for j in range(N)]
    print(li_rev)
    result = ''
    for i in range(N):
        for j in range(N-M+1):
            if check(li[i],j,j+M-1):
                result += ''.join(li[i][j:j+M])
            elif check(li_rev[i],j,j+M-1):
                result += ''.join(li_rev[i][j:j + M])

    print('#{} {}'.format(tc, result))