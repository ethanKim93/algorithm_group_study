import sys
sys.stdin = open("input.txt")

def priority(n):
    if n == '+':
        return 1
    if n == '*':
        return 2

T = 10
for tc in range(1,T+1):
    N = int(input())
    words = input()
    stack = []
    result = []
    for i in range(N):
        if words[i] != '+' and words[i] != '*':
            result.append(words[i])
        elif not stack:
            stack.append(words[i])
        else:
            if priority(stack[-1]) < priority(words[i]):
                stack.append(words[i])
            else:
                while stack and (priority(stack[-1]) >= priority(words[i])):
                    result.append(stack.pop())
                stack.append(words[i])
    while stack:
        result.append(stack.pop())

    for j in range(len(result)):
        if result[j] != '+' and result[j] != '*':
            stack.append(result[j])
        elif result[j] == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif result[j] == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
    print('#{} {}'.format(tc, stack.pop()))




