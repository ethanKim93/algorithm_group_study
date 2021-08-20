import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    text = list(input())
    stack = []



    for txt in text:
        if not stack:
            stack.append(txt)
        elif stack and stack[-1] != txt:
            stack.append(txt)
        else:
            for i in range(len(stack)):
                if stack and stack[i] == txt:
                    stack.pop()
                    break
    # print(stack)
    print("#{} {}".format(tc, len(stack)))
