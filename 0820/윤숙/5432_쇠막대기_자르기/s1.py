import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    poll = list(input())

    stack = []
    count = 0
    for i in range(len(poll)):

        if poll[i] == '(':
            stack.append(poll[i])
            continue
        elif poll[i] == ')':
            if stack:
                if poll[i-1]=='(': #레이저 일때..
                    stack.pop(-1)
                    count+=len(stack) # 쇠막대기의 끝부분일때..
                elif poll[i-1]==')':
                    stack.pop(-1)
                    count+=1



    print('#{} {}'.format(tc,count))

