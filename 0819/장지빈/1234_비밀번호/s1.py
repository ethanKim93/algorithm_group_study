import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    lenN, pw = map(str, input().split())
    stack = []
    for p in range(len(pw)):
        if not stack or pw[p] != stack[-1]:
            stack.append(pw[p])
        else:
            stack.pop()
    ans = ''.join(stack)
    print('#{} {}'.format(tc, ans))