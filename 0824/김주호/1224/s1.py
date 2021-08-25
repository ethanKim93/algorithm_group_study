import sys
sys.stdin = open("input.txt")

for case in range(10):
    input()
    st = input()
    li = []
    op = []
    flag = 0

    for ch in st:
        if "0" <= ch <= "9":
            li.append(int(ch))
        elif ch == "*":
            op.append(ch)
        elif ch == "(":
            op.append(ch)
            flag += 1
        elif ch == ")":
            while op[-1] != "(":
                li.append(op.pop())
            op.pop()
            flag -= 1
        elif flag and ch == "+":
            while op[-1] != "(":
                li.append(op.pop())
            op.append(ch)
        elif (not flag) and ch == "+":
            while op:
                li.append(op.pop())
            op.append(ch)
    li += op

    stack = []
    for ch in li:
        if type(ch) is int:
            stack.append(ch)
        elif ch == "*":
            stack.append(stack.pop(-2) * stack.pop())
        elif ch == "+":
            stack.append(stack.pop(-2) + stack.pop())

    print("#{} {}".format(case + 1, stack[-1]))


