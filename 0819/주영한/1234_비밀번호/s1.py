import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    dum, texts = input().split()
    stack = []
    for text in texts:
        if not stack:
            stack.append(text)
            continue
        if stack[-1] != text:
            stack.append(text)
        else:
            while stack and stack[-1] == text:
                stack.pop(-1)
    print("#{} {}".format(tc, "".join(stack)))