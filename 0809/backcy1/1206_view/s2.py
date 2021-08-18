import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    H = list(map(int, input().split()))

    ans = 0
    for i in range(2, L-2): # 조망권을 고려할 칸 i
        #H[i-2], H[i-1], H[i+1], H[i+2]와 비교
        maxV = H[i-2]
        if maxV < H[i-1]:
            maxV = H[i - 1]
        if maxV < H[i+1]:
            maxV = H[i + 1]
        if maxV < H[i + 2]:
            maxV = H[i + 2]
        if H[i] > maxV:
            ans += H[i] - maxV

    # print(f'#{tc} {view}')             # 3.6이상
    print('#{} {}'.format(tc, ans))     # 3.5에서


