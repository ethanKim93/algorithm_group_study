import sys
sys.stdin = open("sample_input.txt")

def push(a):
    stack.append(a)

def pop():
    if stack:
        return stack.pop()

def check(coms):
    for i in range(len(coms)):
        if coms[i] == '{' or coms[i] == '(':
            push(coms[i])
        # 중괄호 닫힘 검사
        if coms[i] == '}':
            if stack:            # 스택에 원소가 남아있는 경우
                if pop() == '{': # pop해서 나온게 짝이 맞는 경우 pass, 아니면 0 리턴
                    pass
                else:
                    return 0
            else:
                return 0        # 스택에 남아있는게 없으면 0 리턴
        # 소괄호 닫힘 검사
        if coms[i] == ')':
            if stack:
                if pop() == '(':
                    pass
                else:
                    return 0
            else:
                return 0
    if stack:                  # 끝났는데 stack에 남아 있으면
        return 0
    else:                      # stack이 비어있으면 1 출력
        return 1

for tc in range(1, int(input())+1):
    stack = []
    coms = input()
    print('#{} {}'.format(tc, check(coms)))
