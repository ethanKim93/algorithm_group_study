import sys
sys.stdin = open("GNS_test_input.txt")


num_rule = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T+1):
    t, long = map(int, input()[1:].split())
    test_case = list(input().split())


    x = []
    for num in num_rule:
        for case in test_case:
            if num == case:
                x.append(num)

    print('#{}'.format(tc), *x)