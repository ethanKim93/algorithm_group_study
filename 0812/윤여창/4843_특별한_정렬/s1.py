import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    real_li = []

    for i in range(10):
        max_number, min_number = li[0], li[0]
        ix = 0
        if i % 2 == 0:
            for j in range(len(li)):
                if li[j] >= max_number:
                    max_number = li[j]
                    ix = j
        else:
            for j in range(len(li)):
                if li[j] <= min_number:
                    min_number = li[j]
                    ix = j

        real_li.append(li.pop(ix))
    print('#{} {}'.format(tc, real_li))
