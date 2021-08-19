import sys
sys.stdin = open('input.txt')


def erase_repetition(word):
    stack = [word[0]]
    while True:
        for i in range(1, len(word)):
            if stack and word[i] == stack[-1]:
                stack.pop()
                continue
            stack.append(word[i])
        return stack


for tc in range(1, 11):
    N, word = input().split()
    password = erase_repetition(word)
    print('#{} {}'.format(tc, ''.join(password)))