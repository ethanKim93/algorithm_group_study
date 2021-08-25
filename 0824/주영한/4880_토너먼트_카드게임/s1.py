import sys
sys.stdin = open("sample_input.txt")


def divide_cards(cards):
    # 대진표를 생성한다.
    # 초기 스택은 가장 첫번째 인원과 가장 마지작 인원을 두고
    # while문을 통하여 대진표를 만든다
    stack = [1, len(cards)]
    idx = 0

    while idx < len(stack):
        if stack[idx + 1] - stack[idx] > 1:
            front = (stack[idx] + stack[idx + 1]) // 2
            back = (stack[idx] + stack[idx + 1]) // 2 + 1
            stack.insert(idx + 1, back)
            stack.insert(idx + 1, front)
            continue
        idx += 2
    return stack


def games(cards):
    game_table = divide_cards(cards)
    while len(game_table) > 1:
        match = []
        for idx in range(0, len(game_table) - 1, 2):
            # A : 경기에서 앞 번호 사람이 내는 경우
            # B : 경기에서 뒤 번호 사람이 내는 경우
            A = cards[game_table[idx] - 1]
            B = cards[game_table[idx + 1] - 1]

            # 비겼을 경우 번호가 작은 사람이 승자
            if (A == 1 and B == 2) or\
                (A == 2 and B == 3) or\
                (A == 3 and B == 1):
                match.append(game_table[idx + 1])
            else:
                match.append(game_table[idx])
        # 대진표를 업데이트 한다.
        game_table = match

    # 최종 승자를 반환한다.
    return game_table[0]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    print("#{} {}".format(tc, games(cards)))
