import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def tree(i):
    if not i :
        return
    tmp = i//2
    if li[i] > li[tmp]:
        li[i], li[tmp] = li[tmp], li[i]
    while tmp > 1:
        if li[tmp] > li[tmp//2]:
            li[tmp], li[tmp//2] = li[tmp//2], li[tmp]
        tmp // 2
    i -= 1
    tree(i)


for tc in range(1, int(input())+1):
    N = int(input())
    li = [0] + list(map(int, input().split()))
    i = len(li)-1
    # for i in range(i, 0, -1):
    #     for j in range(i):
    #         if li[j] > li[j+1]:
    #             li[j], li[j+1] = li[j+1], li[j]
    tree(i)

    print('#{} {}'.format(tc, li))