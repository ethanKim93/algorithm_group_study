import sys
sys.stdin = open("input.txt")

T = 10


def check(target, left, right):
    while left < right:
        if target[left] == target[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


for _ in range(T):
    tc = int(input())
    N = 100
    li = [input() for _ in range(N)]
    li_rev = [list(li[i][j] for i in range(N)) for j in range(N)]
    result = []
    for pal in range(N - 1, -1, -1):
        for i in range(N):
            for j in range(N-pal+1):
                if check(li[i], j, j + pal -1):
                    result.append(pal)
                elif check(li_rev[i], j, j + pal -1):
                    result.append(pal)
    cnt = result[0]
    for k in range(len(result)):
        if cnt < result[k] :
            cnt = result[k]
    print('#{} {}'.format(tc, cnt))


# 아이디어 : 범위가 아닌 회문 길이를 하나씩 줄여나가기