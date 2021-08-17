import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    dict1 = {}
    dict2 = {}

    for s in str1:
        if s in dict1:
            dict1[s] += 1
        else:
            dict1[s] = 1

    for s in str2:
        if s in dict2:
            dict2[s] += 1
        else:
            dict2[s] = 1

    maxNum = 0
    for key in dict1.keys():
        if key in dict2:
            if maxNum < dict2[key]:
                maxNum = dict2[key]

    print('#{} {}'.format(tc, maxNum))
