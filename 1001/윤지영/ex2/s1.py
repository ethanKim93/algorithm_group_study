import sys
sys.stdin = open('input.txt')

def perm(n,k):
    if k==n:
        per.append(p[:])
        return
    else:
        for i in range(n):
            if used[i] == 0:
                p[k] = num[i]
                used[i] = 1
                perm(n, k+1)
                used[i] = 0

for tc in range(1,int(input())+1):
    num = list(map(int,input()))
    per = []
    p = [0] * 6
    used = [0] * 6
    perm(6,0)
    print('#{}'.format(tc), end=' ')
    for pe in per:
        cnt_run = 0
        cnt_triplet = 0
        for i in [0,3]:
            if pe[i] == pe[i+1] == pe[i+2] :
                cnt_run += 1
            if (pe[i] +1 == pe[i+1]) and (pe[i+1]+1 == pe[i+2]):
                cnt_triplet += 1
        if cnt_run + cnt_triplet == 2:
            print('baby-gin')
            break
    else:
        print('baby-gin이 아님')
    print()







