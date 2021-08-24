import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    st = input().split()
    stack = []

    val = 0
    try:
        for ch in st:
            if "0" <= ch <= "9":
                stack.append(int(ch))
            elif ch == "+":
                stack.append(stack.pop(-2) + stack.pop())
            elif ch == "-":
                stack.append(stack.pop(-2) - stack.pop())
            elif ch == "*":
                stack.append(stack.pop(-2) * stack.pop())
            elif ch == "/":
                stack.append(stack.pop(-2) // stack.pop())
            elif ch == ".":
                if len(stack) == 1:
                    val = stack[0]
                else:
                    val = "error"
                break
    except:
        val = "error"

    print("#{} {}".format(case + 1, val))
