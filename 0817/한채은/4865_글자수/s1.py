import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())    # 찾을 문자열
    str2 = list(input())    # 문자열

    new_d = {}

    # 딕셔너리 만들어서 개수 세주기

    for i in str2:
        if new_d.get(i, 0) == 0:
            new_d[i] = 1
        else:
            new_d[i] += 1

    maxi = 0
    for j in set(str1):
        if maxi <= new_d.get(j):
            maxi = new_d.get(j)

    print('#{} {}'.format(tc, maxi))
