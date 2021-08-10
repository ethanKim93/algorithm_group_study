import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    fall_max = 0
    for i in range(len(li)-1):
        fall = 0
        for j in range(i+1, len(li)):
            if li[i] > li[j]:     # li[0] >li[1], li[0] > li[2] ... 할 때마다 낙차는 +1
                fall += 1     # 즉, li[i]가 li[j]보다 큰 경우마다 한칸씩 떨어질 수 있으므로
        if fall_max < fall:
            fall_max = fall

    print('#{0} {1}'.format(tc, fall_max))