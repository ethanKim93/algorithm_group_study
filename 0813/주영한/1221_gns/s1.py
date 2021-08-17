import sys
sys.stdin = open("GNS_test_input.txt", encoding='UTF8')

alientohuman = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
         "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

humantoalien = dict((value, key) for key, value in alientohuman.items())

T = int(input())
for i in range(T):
    nums = [0] * 10
    tc, L = input().split()
    L = int(L)
    lan_lists = input().split()
    for lan_list in lan_lists:
        nums[alientohuman[lan_list]] += 1

    print(tc)
    for num in range(10):
        for _ in range(nums[num]):
            print(humantoalien[num], end=" ")
    print()

