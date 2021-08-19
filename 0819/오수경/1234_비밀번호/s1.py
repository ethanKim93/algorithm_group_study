import sys
sys.stdin = open('input.txt')

def del_repeat(num):
    stack.append(num[0])

    for word in num[1:]:
        if len(stack) != 0 and stack[-1] == word:
            stack.pop(-1)
        else:
            stack.append(word)
    return stack


for tc in range(1, 11):
    num_len, num = input().split()
    stack = []
    print('#{} {}'.format(tc, ''.join(del_repeat(num))))
