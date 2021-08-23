import sys
sys.stdin = open("input.txt")

def to_postfix(eqn):
    for i in eqn:
        if i == '+': # 이 토큰이 stack의 top에 있는 연산자보다 우선순위가 높으면 stack에 push
            while(stack):   #그렇지 않다면 stack top의 연산자의 우선순위가 높을 때까지 pop
                if stack[-1] == '*':
                    post_eqn.append(stack.pop())
                else:
                    break
            stack.append(i)
        elif i == '*':       # * 는 + 보다 우선순위가 높으므로
            stack.append(i)
        else:
            post_eqn.append(i)

    while(stack):
        post_eqn.append(stack.pop())

    # 후위 표기법의 수식을 스택을 이용하여 계산
    # 피연산자를 만나면 stack에 push, 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop
    # 하여 연산하고, 다시 스택에 push
    # 수식이 끝나면, 마지막으로 스택을 pop 하여 출력
    for i in post_eqn:
        if i == '+':
            stack.append(int(stack.pop())+int(stack.pop()))
        elif i == '*':
            stack.append(int(stack.pop())*int(stack.pop()))
        else:
            stack.append(i)

    return stack.pop()


for tc in range(1, 11):
    N = int(input())
    eqn = input()
    stack, post_eqn = [], []
    print('#{} {}'.format(tc, to_postfix(eqn)))
