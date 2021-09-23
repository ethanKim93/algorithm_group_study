# 푸른놈 -> N, 붉은놈 -> S
import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        stack = []
        for j in range(N):
            if table[j][i]:  # 1아니면 2이면 추출
                stack.append(table[j][i])
        idx = 0
        while idx < len(stack):
            if stack[idx] == 1:  # 2이면 패쓰
                if 2 not in stack[idx:]:  # 모두 통과되어서 공백으로 되는 경우
                    break
                elif stack[idx+1] == 2:
                    ans += 1
                idx += 1
            else:
                idx += 1
    print('#{} {}'.format(tc, ans))




