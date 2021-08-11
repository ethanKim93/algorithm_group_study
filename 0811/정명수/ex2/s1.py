import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):
    numbers = list(map(int, input().split()))
    n = len(numbers)
    result = 0
    for i in range(1<<n):
        club = []
        for j in range(n):
            if i & (1<<j):
                club.append(numbers[j])
        club_sum = 0
        for k in club:
            club_sum += k
        if club_sum == 0:
            result = 1
    print(result)

