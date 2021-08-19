import sys
sys.stdin = open("input.txt")

for _ in range(2):
    brackets = input()
    stack = [0]*len(brackets)
    top = -1
    print('#{} {}'.format(_, brackets), end=" ")
    for bracket in brackets:
        if bracket == '(': # 열린 괄호를 만나는 경우 push
            top += 1
            stack[top] = bracket
        else: # 닫힌 괄호를 만나는 경우 pop
            top -= 1
            if not stack[top+1]: # stack 이 비어있는 경우
                print('Bracket Stack Error: mismatching')
                # raise ValueError
            else:
                stack[top+1] = 0
    else:
        if stack[0]:
            print('Bracket Stack Error: still remaining')
            # raise ValueError
        else:
            print('Bracket Stack is OK')


