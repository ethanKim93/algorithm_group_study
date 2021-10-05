import sys
sys.stdin = open('input.txt')

def bubble(li):
    for i in range(len(li)-1, -1, -1):
        for j in range(i):
            if li[j] <  li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

for tc in range(1, int(input())+1):
    ans = 0
    container, truck = map(int, input().split())
    weight = bubble(list(map(int, input().split())))
    capa = bubble(list(map(int, input().split())))
    cnt = [0] * len(capa)
    # print(container, truck, weight, capa)
    for i in range(len(capa)):
        for j in range(len(weight)):
            if capa[i] >= weight[j]:
                capa[i] = 0
                ans += weight[j]
                weight[j] = 51
                cnt[i] = 1
    print('#{} {}'.format(tc, ans))