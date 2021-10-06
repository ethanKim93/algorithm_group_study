import sys
sys.stdin = open('sample_input.txt', 'r')


def baby_jin(player):
    # 이겼는지 체크를 위한 함수
    for j in range(10):
        # 10장을 돌면서검사
        if player[j] == 3:
            # 만약 같은 카드를 3장 가지고 있으면 이김
            return True

    for k in range(8):
        # 마지막 7,8,9 까지만 검사
        if player[k] and player[k + 1] and player[k + 2]:
            # 연속된다면 이겼으니까 종료
            return True

    return False
    # 승리요건 달성 못함


T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10
    # 각각의 인덱스가 카드번호가 되도록 플레이어들 초기값 생성
    winner = 0
    # 처음 시작은 비기는 걸로

    for i in range(len(nums)):
        # 주어진 카드를 한장씩 나눠준다
        if i % 2 == 0:
            # 먼저 p1부터 받는다
            player1[nums[i]] += 1
            # 카드 번호에 해당하는 p1의 인덱스에 카드 장수를 늘려준다
            if baby_jin(player1):
                # 승리조건을 만족했다면
                winner = 1
                break
        else:
            player2[nums[i]] += 1
            if baby_jin(player2):
                winner = 2
                break

    print('#{} {}'.format(tc, winner))
