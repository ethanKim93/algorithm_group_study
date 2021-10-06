import sys
sys.stdin = open('sample_input.txt')


def check_run_triplet(arr):
    """
    :return: run이거나, triplet 이면,  1반환하기 아니면 0반환
    내가 가진 카드 덱의 순열을 이용한 run/triplet 확인이 아니라...
    각 카드를 몇장 가지고 있는가? 하는 배열을 이용한 확인
    arr : 1~9까지의 카드가 각 몇장씩 있는가 저장하는 배열
    """
    arr.sort()
    for j in range(len(arr) - 2):
        if arr[j] + 2 == arr[j + 1] + 1 == arr[j + 2] or arr[j] == arr[j + 1] == arr[j + 2]:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    # 각 플레이어가.... 돌아가면서 한 장씩 카드를 뽑기
    # 카드를 뽑을 때 마다 카드 덱이 run/ triplet인지 확인하기

    # 카드덱에서 한장씩 확인하면서, winner가 나오면 winner를 바꿔주면 됩니다.
    winner = 0  # 비기면, 0이니까. 0으로 초기화
    # [0,0,0,0,0,0,0,0,0,0]
    p1 = []
    p2 = []
    for i in range(0, len(numbers), 2):
        # 카드 뽑으면서 승자가 나왔는지 확인
        # i 번째 카드가 p1의 카드 >> p1의 카드덱을 만들고
        # check_run_triplet(p1의 카드덱)
        # i + 1 번째 카드가 p2의 카드 >> p2가 카드덱을 만들기
        # check_run_triplet(p2의 카드덱)
        p1.append(numbers[i])
        p2.append(numbers[i + 1])
        if check_run_triplet(p1):
            winner = 1
            break
        if check_run_triplet(p2):
            winner = 2
            break

    print('#{} {}'.format(tc, winner))

