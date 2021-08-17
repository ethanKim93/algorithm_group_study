import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test in range(T):
    pipe = str(input())

    stack = 0           # 쌓인 pipe 개수
    cnt = 0             # 잘린 pipe 개수

    pipe = pipe.replace('()', 'c', pipe.count('()')) # pipe에서 레이저'()'가 나오면 c로 대치

    for p in pipe:
        if p == '(':
            stack += 1
        elif p == ')':
            cnt += 1
            stack -= 1
        else:
            cnt += stack

    print('#{} {}'.format(test+1, cnt))