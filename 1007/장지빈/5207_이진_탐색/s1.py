import sys
sys.stdin = open('input.txt')

def bubble(li):
    for i in range(len(li)-1, -1, -1):
        for j in range(i):
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

def check(n, li):
    global ans
    l = 0
    r = len(li)-1
    m = (l + r) // 2
    flag = True
    subflag = 0
    while flag:
        if li[m] == n:
            ans += 1
            return
        elif li[m] > n:
            if subflag == 1:
                return
            r = m - 1
            m = (l + r) // 2
            subflag = 1
        else:
            if subflag == 2:
                return
            l = m + 1
            m = (l + r) // 2
            subflag = 2
    return

for tc in range(1, int(input())+1):
    ans =  0
    N, M = map(int, input().split())
    Nn = bubble(list(map(int, input().split())))
    Mn = list(map(int, input().split()))
    for m in Mn:
        check(m, Nn)

    print('#{} {}'.format(tc, ans))