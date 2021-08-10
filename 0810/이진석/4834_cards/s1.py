import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    counts = [0] * 10
    cards = list(map(int, list(input())))
    max_cnt = 0
    max_idx = 0
    for card in cards:
        counts[card] += 1
    for idx, count in enumerate(counts):    # 0부터 9까지 순차적으로 비교하기 때문에 동일한 장수의 카드여도 높은 숫자가 적힌 카드가 출력
        if count >= max_cnt:
            max_cnt = count
            max_idx = idx
    print('#{} {} {}'.format(tc, max_idx, max_cnt))