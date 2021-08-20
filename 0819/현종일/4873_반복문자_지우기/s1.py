import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    S = input()
    chars = []
    top = -1

    for char in S:
        if len(chars) and chars[top] == char:
            chars.pop()
            top -= 1
        else:
            chars.append(char)
            top += 1

    print('#{} {}'.format(tc, len(chars)))