import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    patt = input()
    sentence = input()

    if patt in sentence:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))

