
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    text = input()        # ABCCB
    stack = []

    for i in text:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))
