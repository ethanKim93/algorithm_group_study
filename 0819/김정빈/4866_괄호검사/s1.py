import sys
sys.stdin = open("input.txt")
def check(word):
    for w in word:
        if w == '(' or w == '{':
            stack.append(w)
        if w == ')':
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return 1
            else:
                return 1
        if w == '}':
            if len(stack) > 0:
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return 1
            else:
                return 1

    return len(stack)

def isempty(l):
    if l: #0이면
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    print('#{} {}'.format(tc, isempty(check(word))))