for tc in range(1,11):
    N = int(input())
    sik = input()
    number = [str(i) for i in range(10)]
    stack = []
    result = []
    p = {'+': 1, '*': 2}
    for j in sik:
        if j in number:
            result.append(j)
        else:
            if stack:
                if p[j] > p[stack[-1]]:
                    stack.append(j)
                else:
                    while stack:
                        result.append(stack.pop(-1))
                        if stack:
                            if p[stack[-1]] < p[j] :
                                break
                    stack.append(j)

            else:
                stack.append(j)
    while stack:
        result.append(stack.pop())
    stack=[]
    for i in result:
        if i in number:
            stack.append(i)
        else:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                c = int(a) + int(b)
                stack.append(c)
            else:
                a = stack.pop()
                b = stack.pop()
                c = int(a)*int(b)
                stack.append(c)
    print('#{}'.format(tc), end = ' ')
    print(*stack)










