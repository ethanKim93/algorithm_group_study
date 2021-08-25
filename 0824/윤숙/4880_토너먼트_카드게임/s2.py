import sys

sys.stdin = open('input.txt')
##교수님 코드보고 공부하면서 짜본 코드..
def iswinner(player1, player2):

    if arr[player1-1] == 1 and arr[player2-1] == 2:
        return player2
    elif arr[player1-1] == 1 and arr[player2-1] == 3:
        return player1
    elif arr[player1-1] == 2 and arr[player2-1] == 1:
        return player1
    elif arr[player1-1] == 2 and arr[player2-1] == 3:
        return player2
    elif arr[player1-1] == 3 and arr[player2-1] == 1:
        return player2
    elif arr[player1-1] == 3 and arr[player2-1] == 2:
        return player1
    else:
        return player1


def gameplay(start, end):
    if start == end:
        return start
    else:
        player1 = gameplay(start, (start + end) // 2)
        player2 = gameplay((start + end) // 2 + 1, end)

        return iswinner(player1, player2)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    start = 1
    end = N
    print('#{} {}'.format(tc,gameplay(start, end)))
