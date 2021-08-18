import sys
sys.stdin = open("GNS_test_input.txt")

trans = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
reverse = dict(map(reversed, trans.items()))
T = int(input())
for _ in range(T):
    N, L = input().split()
    space_nums = input().split()

    li = []
    for space_num in space_nums:
        li.append(trans[space_num])

    li.sort()
    space_li = []
    for num in li:
        space_li.append(reverse[num])
    print(N)
    print(*space_li)
