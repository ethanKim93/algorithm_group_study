import  sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    cnt = [0] * 10 #0~9까지 카드 개수를 세는 배열 생성
    for i in range(N):
        if cards[i]: #해당 카드가 있다면 cnt배열에 1추가
            cnt[cards[i]] += 1

    max_card_num = cnt[0]
    max_card = 0
    for j in range(1, len(cnt)):
        if max_card_num <= cnt[j]: #cnt배열에서 최대값 최대값이 있는 인덱스 검색
            max_card_num = cnt[j]
            max_card = j
    print('#{} {} {}'.format(tc, max_card, max_card_num))