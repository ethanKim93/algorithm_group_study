import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    cnt_list = [0] * M
    result = cnt_list[0]
    for i in range(N):
        for j in range(M):
            if str1[i] == str2[j]:
                cnt_list[i] += 1
        if cnt_list[i] > result :
            result = cnt_list[i]
    print('#{} {}'.format(tc, result))
