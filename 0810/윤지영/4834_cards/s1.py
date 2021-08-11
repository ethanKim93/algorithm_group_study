import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input()
    counts = [0] * 10
    for chr in cards:
        counts[int(chr)] += 1
    card = cards[0]
    result = counts[0]
    for j in range(10):
        if result <= counts[j]:
            result = counts[j]
            card = j

    print('#{0} {1} {2}'.format(tc, card, result))