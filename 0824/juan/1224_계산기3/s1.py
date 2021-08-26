import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = input()
    eq = input()
    post, stack = [], []                            # post는 후위표기식 스택, stack은 연산자 받을 스택
    for i in eq:
        if i.isdecimal():
            post.append(i)
        else:
            if i == '(':                            # 여는 괄호는 우선순위가 가장 높아서 stack에 바로 추가
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':   # 곱셈 연산자는 stack에 마지막 연산자가 '*'인 동안 
                    post.append(stack.pop())        # 연산자를 꺼내서 post 에 추가한 이후에
                stack.append(i)                     # stack에 추가
            elif i == '+':                          
                while stack and stack[-1] != '(':   # 덧셈 연산자는 우선순위가 낮은 여는 괄호가 나올때까지
                    post.append(stack.pop())        # 연산자를 꺼내서 post 에 추가한 이후에
                stack.append(i)                     # stack에 추가
            else:
                while stack and stack[-1] != '(':   # 닫는 괄호는 여는 괄호 나올때까지
                    post.append(stack.pop())        # 연산자를 꺼내서 post 에 추가한 이후에
                stack.pop()                         # stack 마지막 연산자인 여는 괄호도 pop으로 제거
    while stack:                                    # stack에 연산자가 남아있다면
        post.append(stack.pop())                    # 하나씩 꺼내서 post 에 추가
    # print(post)

    for token in post:                              # 후위표기식 순서로 추가된 post에서 하나씩 꺼내서
        if token.isdecimal():                       # 숫자라면 stack 에 추가
            stack.append(token)
        else:                                       # 연산자라면
            b = int(stack.pop())
            a = int(stack.pop())
            if token == '+':                        # 덧셈 연산자는 더하고 다시 stack 에 추가
                stack.append(a+b)
            else:                                   # 곱셈 연산자는 곱하고 다시 stack 에 추가
                stack.append(a*b)
    print('#{} {}'.format(tc, *stack))


