for tc in range(1, 11):
    N = int(input())
    text = input()
    stack = []
    final = []

    for op in text:
        if op == '(' or op == '*':
            stack.append(op)

        elif op == '+':
            while stack:
                if stack[-1] == '(':
                    break
                final.append(stack.pop())
            stack.append(op)

        elif op == ')':
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
                final.append(stack.pop())

        else:
            final.append(op)

    while stack:
        final.append(stack.pop())

    print(final)

    total = []
    for i in final:
        if i == '+':
            a = total.pop()
            b = total.pop()
            c = int(a) + int(b)
            total.append(c)

        elif i == '*':
            a = total.pop()
            b = total.pop()
            c = int(a) * int(b)
            total.append(c)

        else:
            total.append(i)

    print('#{} {}'.format(tc, total[0]))