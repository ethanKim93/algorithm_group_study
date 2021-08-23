import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    texts = input()
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
    print("#{} {}".format(tc, len(stack)))