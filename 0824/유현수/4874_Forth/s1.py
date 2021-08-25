import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    exp = input().split()
    stack = []
    for i in exp:
        if i.isdigit():                                         # 숫자일 때 스택에 추가
            stack.append(int(i))
        else:                                                   # 연산자일때 스택에서 값을 꺼내 연산
            try:                                                # 연산 수행 시 스택이 비어있으면 except
                if i == '+':
                    stack.append(stack.pop() + stack.pop())

                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)

                elif i == '*':
                    stack.append(stack.pop() * stack.pop())

                elif i == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b // a)
                else:
                    if len(stack) > 1:                              # 스택에 숫자가 1개 이상이면 error
                        print('#{} error'.format(tc))
                        break
                    else:
                        print('#{} {}'.format(tc, stack.pop()))     # 스택이 비어있으면 except
            except:
                print('#{} error'.format(tc))
                break
