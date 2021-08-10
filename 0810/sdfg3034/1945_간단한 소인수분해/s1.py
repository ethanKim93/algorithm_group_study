import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(1,T+1):
    N = int(input())

    insu_data = [2,3,5,7,11]
    data=[0]*5
    j = 0
    while N != 1:
        if N % insu_data[j] == 0:
            data[j] += 1
            N /= insu_data[j]
        else:
            j += 1
    print('#{}'.format(i), end=" ")
    print(*data)
