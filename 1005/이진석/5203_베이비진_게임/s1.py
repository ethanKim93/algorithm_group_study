import sys

sys.stdin = open('sample_input.txt')


def babygin(num, player):
    if player % 2:  # 전달받은 player 인자가 홀수일때 : 짝수번째카드, 2번플레이어
        card = c2   # 플레이어 카드 shallow copy (주소 공유, 같은 value를 가짐)
        player = 2  # 플레이어 번호
    else:           # 홀수번째카드, 1번플레이어
        card = c1
        player = 1
    card[num] += 1  # 입력받은 카드 번호를 인덱스로 card ++ (카드 장수 ++)

    if card[num] >= 3:                                                      # triplet
        return player
    elif num <= 7 and card[num] and card[num + 1] and card[num + 2]:        # 들어온카드,+1,+2 (run)
        return player
    elif 1 <= num <= 8 and card[num-1] and card[num] and card[num + 1]:     # -1,들어온카드,+1 (run)
        return player
    elif num >= 1 and card[num-2] and card[num-1] and card[num]:            # -2,-1,들어온카드 (run)
        return player

    return

for tc in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))     # 순서대로 들어올 카드 리스트
    c1 = [0] * 10                               # 1번 플레이어의 카드
    c2 = [0] * 10                               # 2번 플레이어의 카드
    for i in range(len(cards)):                 # 카드 한장마다
        answer = babygin(cards[i], i)           # baby-gin 확인
        if answer:                              # return값이 있을 때 종료
            print('#{} {}'.format(tc, answer))
            break
    else:
        print('#{} {}'.format(tc, 0))

