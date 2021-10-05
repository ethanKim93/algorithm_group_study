import sys
sys.stdin = open('sample_input.txt')


def babygin(lst_a, lst_b, cnt):
    if cnt >= 3:
        for i in range(9):
            if lst_a[i] >= 3:
                return 1

        for j in range(8):
             if ''.join(lst_b[j:j+3]) == '111':
                 return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1_triplet = [0]*10
    p1_run = ['0'] * 10
    p2_triplet = [0]*10
    p2_run = ['0'] * 10

    ans = 0
    for i in range(6):
        p1_triplet[cards[2*i]] += 1
        p1_run[cards[2 * i]] = '1'
        if babygin(p1_triplet, p1_run, i):
            print('#{} 1'.format(tc))
            ans += 1
            break

        p2_triplet[cards[2*i+1]] += 1
        p2_run[cards[2 * i + 1]] = '1'
        if babygin(p2_triplet, p2_run, i):
            print('#{} 2'.format(tc))
            ans += 1
            break

    if ans == 0:
        print('#{} 0'.format(tc))


