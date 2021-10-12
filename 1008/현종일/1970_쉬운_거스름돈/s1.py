import sys
sys.stdin = open("input.txt")

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, int(input())+1):
    print('#{}'.format(tc))
    N = int(input())//10*10
    result = [0] * 8

    for i in range(len(money)):
        while N >= money[i]:
            N -= money[i]
            result[i] += 1
    print(*result)

