import sys
sys.stdin = open("input.txt")

def postfix_tocalc(eqn):
    stack, post_eqn = [], []
    isp = {'(':0, '*':2, '+':1}
    icp = {'(':3, '*':2, '+':1}

    for i in eqn:
        if i.isdigit():             #피연산자인 경우 출력 -> 후위연산식으로 push
            post_eqn.append(i)

        elif i == ')':              #닫는 괄호인 경우 여는 괄호가 나올 때까지 stack에서 pop하고 출력
            while(stack[-1] != '('):
                post_eqn.append(stack.pop())
            if stack[-1] == '(':    #여는 괄호가 stack에 나온 경우 stack에서 pop
                stack.pop()

        else:                       # 나머지 연산자의 경우
            while(stack):           # stack에 있으면 
                if isp[stack[-1]] < icp[i]: # 연산 우선순위 비교 후 들어가는 연산자가 우선하면 stack에 push
                    stack.append(i)
                    break
                else:               # 우선순위가 밀리면 나올 때까지 stack에서 pop한 후 출력
                    post_eqn.append(stack.pop())

            if not stack:           # stack이 비어있으면 append
                stack.append(i)

    while(stack):
        post_eqn.append(stack.pop())

    for i in post_eqn:
        if i.isdigit():
            stack.append(i)    
        elif len(stack) > 1:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '+':
                stack.append(a+b)
            elif i == '*':
                stack.append(a*b)
    return stack.pop()
        


for tc in range(1, 11):
    N = input()
    eqn = input()
    print('#{} {}'.format(tc, postfix_tocalc(eqn)))
    
    
    
