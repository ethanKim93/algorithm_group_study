for case in range(10):
    N = int(input())
    st = input()

    rst = []
    op = []

    for ch in st:
        if "0" <= ch <= "9":
            rst.append(int(ch))
        elif op and ch == "+":
            while op:
                rst.append(op.pop())
            op.append(ch)
        else:
            op.append(ch)

    while op:
        rst.append(op.pop())

    stack = []
    for ch in rst:
        if type(ch) is int:
            stack.append(ch)
        elif ch == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(stack.pop() + stack.pop())

    print("#{} {}".format(case + 1, stack[0]))
