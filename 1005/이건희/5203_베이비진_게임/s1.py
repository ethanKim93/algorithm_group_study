import sys
sys.stdin = open("input.txt")

def check_winner(alist):
    alist = sorted(alist)
    for i in range(len(alist)-2):
        if alist[i] == alist[i+1] == alist[i+2]: # triplet
            return 1
        elif alist[i]+1 == alist[i+1] == alist[i+2]-1: # run
            return 1
    return 0

t = int(input())
for tc in range(1, t+1):
    maps = list(map(int,input().split()))
    player1 = []
    player2 = []
    for i in range(0,12,2):
        player1.append(maps[i])
        player2.append(maps[i+1])

    list1 = [player1.pop(0),player1.pop(0)]
    list2 = [player2.pop(0),player2.pop(0)]
    ans = 0

    for i in range(4):
        list1.append(player1.pop(0))
        list2.append(player2.pop(0))
        result1 = check_winner(list1)
        result2 = check_winner(list2)

        if result1 or result2:
            if result1 == result2:
                ans = 1
            elif result1 > result2:
                ans = 1
            else:
                ans = 2
            break

    print("#{} {}".format(tc, ans))

# Fail: Wrong Anwer + Hard to recognize to others