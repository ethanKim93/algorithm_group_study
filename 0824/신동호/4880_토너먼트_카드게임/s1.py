import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    card_dict = {}
    for i in range(1, N+1):
        card_dict[i] = cards[i-1]
    print(card_dict)
