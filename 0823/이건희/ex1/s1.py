def example(sl):
    sl = list(sl)
    operand = [str(i) for i in range(10)]
    ans = []
    stack = []
    for i in sl:
        if i in operand:
            ans.append(i)
        else:
            stack.append(i)

    while stack:
        ans.append(stack.pop())

    return ans

print(*example('2+3*4/5'))
