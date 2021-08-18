import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = input()
    dict = {}

    for i in range(len(str1)):
        dict[str1[i]] = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dict[str1[i]] += 1
    print('#{} {}'.format(tc,max(dict.values())))



    