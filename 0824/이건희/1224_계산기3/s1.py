import sys

sys.stdin = open("input.txt")

for tc in range(1, 11):
    n = int(input())
    maps = list(input())
    operand = [str(i) for i in range(10)]
    stack = []
    subans = []

    # 중위 -> 후위
    for i in maps:
        if i == "+":
            while stack:
                cold = stack.pop()
                if cold == "(":
                    stack.append(cold)
                    break
                subans.append(cold)
            stack.append(i)

        elif i == "*":
            while stack and stack[-1] == "*":
                subans.append(stack.pop())
            stack.append(i)

        elif i == "(":
            stack.append(i)

        elif i == ")":
            while stack:
                cold = stack.pop()
                if cold == "(":
                    break
                subans.append(cold)

        elif i in operand:
            subans.append(i)

    while stack:
        subans.append(stack.pop())

    # 후위 -> Calculate
    for i in subans:
        if i in operand:
            stack.append(int(i))
        elif i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "*":
            stack.append(stack.pop() * stack.pop())

    print("#{} {}".format(tc, stack[-1]))
