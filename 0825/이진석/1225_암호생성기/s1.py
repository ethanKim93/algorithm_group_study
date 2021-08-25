import sys
sys.stdin = open('input.txt')

def cycle():
    for i in range(1, 6):
        temp = data.pop(0)  # deQ
        if temp-i < 1:      # 감소한 값이 0 이하라면
            data.append(0)  # 0을 enQ하고 cycle을 종료
            return
        else:
            data.append(temp-i) # 감소한 값을 enQ


for _ in range(1, 11):
    tc = int(input())
    data = list(map(int,input().split()))    # 입력 데이터, 큐
    while data[-1] != 0:    # 0이 enQ된다면 종료
        cycle()
    answer = ' '.join(map(str,data))
    print('#{} {}'.format(tc,answer))