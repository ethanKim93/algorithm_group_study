import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = list(map(int, input().split()))
    l = [1, 1]
    r = [N[0], N[0]]
    winner = 0
    breaker = True

    while breaker:
        for i in range(2):
            c = int((l[i] + r[i]) / 2)

            if N[i+1] == c:
                if not i:
                    winner += 1
                else:
                    winner += 2
            elif c > N[i+1]:
                r[i] = c
            else:
                l[i] = c

        if not winner == 0:
            if winner == 1:
                winner = 'A'
            elif winner == 2:
                winner = 'B'
            else:
                winner = '0'
            breaker = False

    print('#{} {}'.format(tc,winner))

