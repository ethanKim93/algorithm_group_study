import sys
sys.stdin = open("GNS_test_input.txt")


num_rule = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T+1):
    t, long = map(int, input()[1:].split())
    test_case = list(input().split())

    for num in num_rule:
        for l in range(long-1):
            min_idx = l
            for case in range(l+1, long):
                if test_case[case] == num:
                    min_idx = case
                    break
            test_case[l], test_case[min_idx] = test_case[min_idx], test_case[l]

    # for l in range(long - 1):
    #     min_idx = l
    #     for case in range(l + 1, long):
    #         if num_rule.index(test_case[case]) < num_rule.index(test_case[l]):
    #             min_idx = case
    #             break
    #     test_case[l], test_case[min_idx] = test_case[min_idx], test_case[l]

    print(test_case)