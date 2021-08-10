import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    def cal(x, y):
        cnt = 0
        while not x % y:
            x /= y
            cnt += 1
        return cnt

    ans = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    for key in ans:
        ans[key] = cal(N, key)

    print('#{} {} {} {} {} {}'.format(tc, ans[2], ans[3], ans[5], ans[7], ans[11],))