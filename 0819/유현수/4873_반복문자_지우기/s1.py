import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = []
    for char in s:                          # 입력된 글자 순회
        if stack:                           # 스택이 비어있지 않으면
            if stack[-1] == char:           # top과 현재 글자가 같은면 pop
                stack.pop()
            else:                           # top과 현재 글자가 다르면 push
                stack.append(char)
        else:                               # 스택이 비어 있으면 push
            stack.append(char)
    print('#{} {}'.format(tc, len(stack)))