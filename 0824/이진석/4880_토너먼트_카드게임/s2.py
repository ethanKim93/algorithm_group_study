import sys

sys.stdin = open('sample_input.txt')

def winner(A,B):
    # if tournament[A] == tournament[B]:
    #     return A
    # elif tournament[A] == 1 and tournament[B] == 2:
    #     pass
    # elif tournament[A] == 1 and tournament[B] == 3:
    #     pass
    # elif tournament[A] == 2 and tournament[B] == 3:
    #     pass
    # elif tournament[A] == 2 and tournament[B] == 1:
    #     pass
    # elif tournament[A] == 3 and tournament[B] == 1:
    #     pass
    # elif tournament[A] == 3 and tournament[B] == 2:
    #     pass
    if (tournament[A] - tournament[B]) % 3 < 2:
        return A
    return B
def vs(start, end):
    if start == end:    # 재귀를 돌며 left, right vs의 인자가 같아질 때 재귀 종료
        return end
    left = vs(start, (start + end) // 2)  # 왼쪽그룹
    right = vs((start + end) // 2+1, end)  # 오른쪽그룹
    return winner(left, right)

for tc in range(1, int(input()) + 1):
    N = int(input())
    tournament = [0] + list(map(int, input().split()))  # 1번부터 활용하기위해 0번 추가
    print('#{} {}'.format(tc,vs(1,N)))

