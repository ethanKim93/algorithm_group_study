import sys
sys.stdin = open("sample_input.txt")

T = int(input())


def pop():
    global top
    top -= 1
    return stack.pop(top+1)


for tc in range(1, T+1):
    stack = []
    top = -1
    result = 1
    code = input()
    N = len(code)
    for i in range(N):
        if (code[i] == '(') or (code[i] == '{'):
            stack.append(code[i])
            top += 1
        elif code[i] == ')':
            if (not stack) or (pop() != '('):
                result = 0
                break
        elif code[i] == '}':
            if (not stack) or (pop() != '{'):
                result = 0
                break
    if stack:
        result = 0
    print('#{} {}'.format(tc, result))


# def check(target, search):
#     if code[i] == target:
#         for t in range(N):
#             if pop() == search:
#                 return True
#         else:
#             return False











