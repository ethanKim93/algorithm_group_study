# 보충 풀이
import sys
sys.stdin = open('sample_input.txt')

def chk(cntlst):
    for i in range(10):
        if cntlst[i] >= 3:
            return True
        if cntlst[i] >= 1 and cntlst[i+1] >= 1 and cntlst[i+2] >= 1:
            return True

    return False

TC = int(input())
for tc in range(1, TC+1):
    lst = list(map(int, input().split()))
    # lst1 = lst[::2]
    # lst2 = lst[1::2]
    # print(lst1, lst2)

    cntlist1 = [0] * 12  # player1을 위한 count 배열
    cntlist2 = [0] * 12  # player2를 위한 count 배열

    winner = 0
    for i in range(6):
        data1 = lst[i*2]
        data2 = lst[i*2+1]
        cntlist1[data1] += 1  # = player1의 cntlist를 만든다
        if chk(cntlist1):
            winner = 1
            break
        cntlist2[data2] += 1  # = player2의 cntlist를 만든다
        if chk(cntlist2):
            winner = 2
            break

    print('#{} {}'.format(tc, winner))