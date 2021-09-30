import sys
sys.stdin = open('input.txt')

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
pwd = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    cnt = 0
    check = []
    ans = []

    for i in range(N):
        for j in range(M):
            # i가 0, j가 0인경우 0,-1이므로 -1-j를 해야한다.
            if arr[i][-1-j] == '1':
                check = arr[i][-j-56:-j]
                cnt += 1
                break

    for i in range(0, len(check), 7):
        code_seven = check[i:i+7]
        # print(code_seven)
        for j in range(10):
            if pwd[j] in code_seven:
                ans.append(j)

    if ((((ans[0] + ans[2] + ans[4] + ans[6])*3) + (ans[1] + ans[3] + ans[5]) + ans[7]) % 10) == 0:
        print('#{} {}'.format(tc, sum(ans)))
    else:
        print('#{} {}'.format(tc, 0))







