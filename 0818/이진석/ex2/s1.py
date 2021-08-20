import sys
sys.stdin = open('input.txt')

for _ in range(3):
    case = input()
    stack = []
    top = -1
    flag = True
    for char in case:
        if char == '(':                           # 괄호가 열릴 때 push
            stack.append(char)
            top += 1
        else:
            if top > -1 and stack[top] == '(':    # 괄호가 닫힐 때 인덱스 유효성검사, 괄호의 짝 검사 후 pop
                stack.pop(top)
                top -= 1
            else:                                 # 이외 케이스들은 모두 짝이 맞지 않는다.
                flag = False
                break
    if len(stack):                                # 마지막 괄호 조사 후에 스택에 괄호가 남아있으면 짝이 맞지 않음
        flag = False
    print(flag)