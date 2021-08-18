import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    sentence, patt = input().split()
    a = sentence.count(patt)

    cunt = len(sentence) - (len(patt) * a) + (1 * a)

    print('#{} {}'.format(tc, cunt))