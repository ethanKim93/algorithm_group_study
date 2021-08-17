import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())
Alien_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    number_len = input()
    number_list = list(map(str, input().split()))

    sort_list = []

    for i in range(10):
        for j in number_list:
            if Alien_number[i] == j:
                sort_list.append(j)

    print('#{}'.format(tc))
    print(*sort_list)