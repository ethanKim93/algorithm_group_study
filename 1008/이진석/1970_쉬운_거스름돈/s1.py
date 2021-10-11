import sys
sys.stdin = open('input.txt', 'r')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, int(input())+1):
    N = int(input())
    answer = []
    for m in money:
        answer.append(N//m)
        N %= m
    answer = ' '.join(map(str, answer))
    print('#{}\n{}'.format(tc, answer))