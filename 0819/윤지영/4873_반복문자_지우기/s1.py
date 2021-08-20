import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    words = input()
    stack = []
    i = 0
    while i < len(words):                   # for i in words 로 해서 words[i] -> i로 변경해서 가능
        if (not stack) or (words[i] != stack[-1]):
            stack.append(words[i])
        else:
            stack.pop()
        i += 1
    print('#{} {}'.format(tc, len(stack)))

