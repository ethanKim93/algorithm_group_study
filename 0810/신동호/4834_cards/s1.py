import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()
    cnts = [0]*10
    for card in cards:
        cnts[int(card)] += 1
    max_n = cnts[0]
    big_n = 0
    for ind in range(10):
        if max_n <= cnts[ind]:
            max_n = cnts[ind]
            big_n = ind
    print('#{} {} {}'.format(tc, big_n, max_n))