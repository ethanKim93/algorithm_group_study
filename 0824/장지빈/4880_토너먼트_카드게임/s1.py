import sys
sys.stdin = open('input.txt')

# 망함
# def whoiswinner(a, b):
#     if a == '1':
#         if b == '2':
#             return b
#         else:
#             return a
#     elif a == '2':
#         if b == '3':
#             return b
#         else:
#             return a
#     else:
#         if b == '1':
#             return b
#         else:
#             return a
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     cards = input().split()
#     middle = len(cards)//2
#     idx = list(range(1, N))
#     leftgame = cards[0:middle]
#     rightgame = cards[middle:]
#     whoiswinner()
#
#     print('#{} {}'.format(tc, tc))

def winner(l, r):
    if (tournament[l] - tournament[r]) % 3 < 2:     # 가위바위보의 승자를 한번에 리턴하는 방법
        return l                                    # 아니면 하나씩 선언
    return r
    # if tournament[l] == tournament[r]:
    #     return l
    # elif tournament


def vs(start, end):
    if start == end:
        return start # end와 같으니까 상관없음
    left = vs(start, (start+end)//2)            #tc1 vs(1,2)    -> vs(1,1)
    right = vs(((start + end) // 2) + 1, end)    #tc1 vs(3,4)    -> vs(2,2)
    # 같아질 때까지 반복해서 한명이 남으면 그걸 올린다
    # 같아질 때까지 계속 재귀.. 같아지면 올라와서 match를 하고 그중에 하나를 return
    return winner(left, right)
for tc in range(1, int(input())+1):
    N = int(input())
    tournament = [0] + list(map(int, input().split()))

    print('#{} {}'.format(tc, vs(1, N)))