import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    days = int(input())
    costs = list(map(int, input().split()))

    income = 0
    max = costs[-1]

    for j in range(days - 2, -1, -1):
        if (costs[j] > max):
            max = costs[j]
        income += (max - costs[j])

    print('#{} {}'.format(tc, income))