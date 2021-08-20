import sys
sys.stdin = open('sample_input.txt')


def erase_repetition(word):
    stack = [word[0]]
    while True:
        for i in range(1, len(word)):
            if stack and word[i] == stack[-1]:
                stack.pop()
                continue
            stack.append(word[i])
        return len(stack)


T = int(input())
for tc in range(1, T+1):
    word = input()
    ans = erase_repetition(word)
    print('#{} {}'.format(tc, ans))