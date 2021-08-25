import sys
sys.stdin = open("input.txt")
for tc in range(1, 11):
    N = int(input())
    text = input()

    res = []
    stack = []
    for i in text:
        if i == "(" or i == "*":
            stack.append(i)
        elif i == "+":
            while stack:
                op = stack.pop()
                if op == "*":
                    res.append(op)
                elif op == "+":
                    res.append(op)
                elif op == "(":
                    stack.append(op)
                    break
            stack.append(i) #stack의 마지막이 (이니까 걍 붙임
        elif i == ")":
            while stack:
                op = stack.pop()
                if op == "(":
                    break
                res.append(op)
        else:
            res.append(i)

    while stack:
        res.append(stack.pop())

    total = []
    for j in res:
        if j == '+':
            a = int(total.pop())
            b = int(total.pop())
            total.append(a + b)
        elif j == '*':
            c = int(total.pop())
            d = int(total.pop())
            total.append(c * d)
        else:
            total.append(j)

    print('#{} {}'.format(tc, *total))