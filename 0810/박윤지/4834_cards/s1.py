import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = input()
    cards = []
    # 연속된 숫자로된 카드들을 하나씩 분리해서 cards 리스트에 담기
    for i in range(0, len(a)):
        cards.append(int(a[i:i+1]))

    # 숫자별로 나온 횟수 저장하는 리스트 counts 만들기
    counts = [0] * 10
    for card in cards:
        counts[card] += 1

    # 횟수가 같다면 가장 오른쪽에 있는(가장 카드 숫자가 큰) 카드가 선택되도록 for문 돌리기
    max_idx = 0
    max_cnt = counts[0]
    for idx in range(0, 10):
        if counts[idx] >= max_cnt:
            max_cnt = counts[idx]
            max_idx = idx
    print('#{} {} {}'.format(tc, max_idx, max_cnt))