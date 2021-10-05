import sys             ###### 실패! 당장 가장 큰 수를 만드는 알고리즘이라서 실패입니다.
sys.stdin = open('input.txt')
def change_num(N):
    number = 0
    for i in range(len(N)-1,-1,-1):
        number += int(N[i])*(10**(len(N)-1-i))
    return number

def makemax(N,r):
    global max_num,present
    if r == counter:
        if now
        max_num = N
        return
    if len(N) > 3 and N[:-2] == sorted(N)[::-1][:-2]:
        N[len(N)-1], N[len(N)-2] = N[len(N)-2], N[len(N)-1]
        makemax(N,r+1)
    else:
        for i in range(len(N)-2):
            if max(N[i:]) == N[i]:
                continue
            else:
                k = N[len(N)-1:i:-1].index(max(N[len(N)-1:i:-1]))
                ks = N[len(N)-1:i:-1].count(max(N[len(N)-1:i:-1]))
                    for j in range(ks):
                        k = len(N)-1-k
                        N[i],N[k] = N[k],N[i]
                        makemax(N,r+1)
                        N[i],N[k] = N[k],N[i]

T = int(input())
for tc in range(1,T+1):
    num, counter = input().split()
    num = list(num)
    present = []
    counter = int(counter)
    max_num = num
    makemax(num,0)
    if len(max_num) == 2:
        if counter%2:
            max_num[0],max_num[1] = max_num[1],max_num[0]
    print('#{} {}'.format(tc,change_num(max_num)))
