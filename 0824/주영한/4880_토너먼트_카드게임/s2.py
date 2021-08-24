import sys
sys.stdin = open("sample_input.txt")

def winner(left, right):
    A = cards[left - 1]
    B = cards[right - 1]

    # 비겼을 경우 번호가 작은 사람이 승자
    if (A == 1 and B == 2) or \
            (A == 2 and B == 3) or \
            (A == 3 and B == 1):
        return right
    else:
        return left

def vs(start, end):
    if start == end:
        return start
    left = vs(start, (start+end)//2)
    right = vs((start+end)//2 + 1, end)
    return winner(left, right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    print("#{} {}".format(tc, vs(1, N)))
