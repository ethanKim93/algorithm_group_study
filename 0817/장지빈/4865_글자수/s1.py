import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = {}

    for i in range(len(str1)):
        cnt[str1[i]] = 0
    # print(cnt)
    for j in range(len(str2)):
        try:
            if cnt[str2[j]] >= 0:
                cnt[str2[j]] += 1
        except:
            pass
    maxstr = 0
    for a in cnt.values():
        if maxstr < a:
            maxstr = a

    print('#{} {}'.format(tc, maxstr))