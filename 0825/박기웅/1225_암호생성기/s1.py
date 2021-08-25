import sys
sys.stdin = open("input.txt")

def crypto():
    front, rear = -1, 7             # front, rear 8개의 숫자에 맞게 초기화

    while 1:                        # return 될 때까지 사이클 반복
        for i in range(1, 6):
            front += 1              # pop을 위해 front += 1
            if arr[front] - i <= 0: # 첫 원소 - i 가 0보다 작은 경우(x) 작거나 같을 경우(o)로 해야 정상 출력
                return arr[front+1:rear+1]+[0]  #그 다음 원소부터 ~ 마지막 원소 + 0
            else:
                rear += 1           # 첫 원소 -i 가 0 보다 큰 경우 enqueue
                arr.append(arr[front]-i)

for _ in range(10):
    tc = input()
    arr = list(map(int, input().split()))
    print('#{}'.format(tc), end=' ')
    print(*crypto())



