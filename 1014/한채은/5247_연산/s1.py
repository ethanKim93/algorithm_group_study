import sys
sys.stdin = open('sample_input.txt')

# check 를 1000001으로 잡으면 런타임 에러 발생,,
# (M*2)+1로 범위 수정.
def bfs(n):
    # ans 불러오고
    global ans
    q = [n]
    # q에 뭐가 있으면
    while q:
        # x 에 q에서 pop한거 넣어주고
        x = q.pop(0)
        # x가 내가 만들 수랑 같아지면
        if x == M:
            # ans에 update 해주고
            ans = check[x]
            # 멈추기
            break
        # 그게 아니면
        else:
            # 연산 돌면서
            for nx in (x+1, x-1, 2*x, x-10):
                # 범위안에 들어가있고, 아직 확인하지 않은 숫자라면?
                if 0 < nx <= size and not check[nx]:
                    # check 연산 위치에 표시 남겨주기
                    check[nx] = check[x] + 1
                    # 다시 q에 연산 쌓아주기
                    q.append(nx)

T = int(input())
for tc in range(1, T+1):
    # N에 연산을 더해 M 만들기
    N, M = map(int, input().split())
    # 최소 연산 구하기
    ans = 10000
    # 원래 (M*2) + 1 이었는데 N이 M보다 큰 경우를 고려해줘야함
    # tc에는 없지만 N이 M보다 큰 경우, ex 9, 1 일 때 M*2 +1로 하면 check 자리가 부족하니까 size 자리 만들어주기.
    if N > M:
        size = N * 2
    else:
        size = M * 2
    # check
    check = [0] * (size + 1)
    # bfs 타기
    bfs(N)
    print('#{} {}'.format(tc, ans))