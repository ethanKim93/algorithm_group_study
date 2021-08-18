import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    arr = [0]*len(str1)

    for i in range(len(str2)):
        for j in range(len(str1)):
            if str1[j] == str2[i]:
                arr[j] += 1

    max_cnt = 0
    for i in arr:
        if max_cnt < i:
            max_cnt = i

    print('#{} {}'.format(tc, max_cnt))
