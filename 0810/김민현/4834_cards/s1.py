import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ai = input()

    #숫자를 구분하고, int형으로 변환
    card_list = []
    len(ai)
    for card in ai:
        card_list.append(int(card))

    # 각 숫자별 회수 파악
    card_cnt = [0]*10
    for i in range(N):
        card_cnt[card_list[i]] += 1

    #가장 많은 빈도수 파악
    cnt_max = card_cnt[0]
    for i in card_cnt:
        if cnt_max < i:
            cnt_max = i
    #동일 빈도수 파악
    result_list=[]
    for idx,cnt in enumerate(card_cnt):
            if cnt_max == cnt:
                result_list.append(idx)
    #리스트에서 가장 끝값(가장 큰값) 출력
    print('#{0} {1} {2}'.format(tc,result_list[-1],cnt_max))