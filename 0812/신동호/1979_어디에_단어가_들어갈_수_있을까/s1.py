import sys
sys.stdin = open('input.txt')

T = int(input())
T=1
for tc in range(1, T+1):
    cnt_r = cnt_c = 0
    N, K = list(map(int, input().split()))
    # print(['0'*(N+2)]+["".join(input().split())+'0' for _ in range(N)])
    boxes = ['0'*(N+2)] +["".join(input().split())+'0' for _ in range(N)] + ['0'*(N+2)]
    print(boxes)
    for box in boxes:
        for i in range(len(boxes)-5):
            if (14<<i & int(box,2))%7 and (14<<i & int(box,2)):
                cnt_r += 1
    print(cnt_r)
    # for ind in range(boxes)
