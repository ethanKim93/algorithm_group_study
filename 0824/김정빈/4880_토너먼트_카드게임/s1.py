import sys
sys.stdin = open("input.txt")
#4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

def group(cards):
    #사람 나누는 함수
    mid = len(cards) // 2
    if len(cards) > 1:
        if len(cards) % 2 == 0:
            newg = group(cards[:mid]), group(cards[mid:])
        else:
            newg = group(cards[:mid+1],cards[mid+1:])
    else:
        return cards
    return newg

def game(groups):
    #대결하는 함수
    if len(group) == 1:
        return




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    # 1: 가위 2: 바위 3: 보
    # print(cards[:N//2], cards[N//2:])
    print(group(cards))