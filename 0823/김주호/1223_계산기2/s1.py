op_upper = ["*", "/"]

for case in range(1):
    N = int(input())
    st = input()

    stack = []
    op = []

    for ch in st:
        if "0" <= ch <= "9":
            stack.append(ch)
        elif op and not(op[-1] not in op_upper and ch in op_upper):
            while op:
                stack.append(op.pop())
            op.append(ch)
        else:
            op.append(ch)

    while op:
        stack.append(op.pop())
    print(stack)
