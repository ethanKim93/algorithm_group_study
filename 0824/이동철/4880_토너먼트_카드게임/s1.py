import sys
sys.stdin = open('input.txt')


def rockscisorpaper(l_idx, r_idx):
    l, r = card[l_idx-1], card[r_idx-1]
    if l == r:
        return l_idx
    elif l == 1: # 가위
        if r == 3:
            return l_idx
        elif r == 2:
            return r_idx
    elif l == 2: # 바위
        if r == 1:
            return l_idx
        elif r == 3:
            return r_idx
    elif l == 3: # 보
        if r == 2:
            return l_idx
        elif r == 1:
            return r_idx


def cardgroup(left, right):
    if left == right:
        return left
    else:
        middle = (left + right) // 2
        l = cardgroup(left, middle)
        r = cardgroup(middle + 1, right)
        return rockscisorpaper(l, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))

    print('#{} {}'.format(tc, cardgroup(1, N)))