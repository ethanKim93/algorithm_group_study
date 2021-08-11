import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    for row in range(100):
        sumthing = 0
        for i in arr[row]:
            sumthing += i
        if sumthing > max_sum:
            max_sum = sumthing

    for col in range(100):
        sumthing = 0
        for i in range(100):
            sumthing += arr[i][col]
        if sumthing > max_sum:
            max_sum = sumthing

    sumthing = 0
    for i in range(100): # 대각선
        sumthing += arr[i][i]
    if sumthing > max_sum:
        max_sum = sumthing
    sumthing = 0
    for i in range(100): # 반대 대각선
        sumthing += arr[99-i][i]
    if sumthing > max_sum:
        max_sum = sumthing
    print('#{}'.format(test_case),end=' ')
    print(max_sum)




