import sys
sys.stdin = open('sample_input.txt')


def rps(i, j):  # 가위바위보
    if cards[i-1] == cards[j-1]:
        return i
    elif cards[i-1] == 1 and cards[j-1] == 3:
        return i
    elif cards[i-1] == 2 and cards[j-1] == 1:
        return i
    elif cards[i-1] == 3 and cards[j-1] == 2:
        return i
    else:
        return j


def winner(s, e):  # 잘라서 둘이 가위바위보
    if s == e:
        return s
    else:
        fir = winner(s, (s+e)//2)
        sec = winner((s+e)//2+1, e)
        return rps(fir, sec)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    win = winner(1, N)
    print('#{} {}'.format(tc, win))

'''
예시
N = 4, cards = 1 3 2 1, winner(맨앞사람,맨뒤사람)
winner(1,4) => fir = winner(1,2), sec = winner(3,4)로 나뉨
winner(1,2) => fir = winner(1,1) == 1, sec = winner(2,2) == 2 => 가위바위보 진행 => 1번째 사람이 이김
winner(3,4) => fir = winner(3,3) == 3, sec = winner(4,4) == 4 => 가위바위보 진행 => 3번째 사람이 이김
따라서 fir = 1, sec = 3이 되어 rps(1,3)은 1이 이긴다.
'''

