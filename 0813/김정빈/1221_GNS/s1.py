import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
for tc in range(1, T+1):
    t, L = map(str, input().split())
    text = list(map(str, input().split()))

    gns = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
    gns2 = {}
    for k, v in gns.items():
        gns2[v] = k

    li = []

    for txt in text:
        li.append(gns[txt])
        li.sort()

        res = []
        for i in li:
            res.append(gns2[i])
    print(t)
    print(*res, sep=" ")