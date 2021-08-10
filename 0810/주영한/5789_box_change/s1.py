import sys
sys.stdin = open('sample_input.txt')

#Test Case 갯수를 입력 받음
T = int(input())

for tc in range(1, T+1):
    # 두 번째 입력인 N개의 상자와, Q회를 입력으로 받음.
    N, Q = map(int, input().split())
    # 0으로 적혀있는 N개의 박스
    boxes = [0] * N
    for i in range(1, Q + 1):
        # i 번째 작업에 대한 정의( 1 <= i <= Q)
        L, R = map(lambda x: int(x) - 1, input().split())
        # 인덱스를 조절해준다(박스의 경우 1번부터 N번까지이고, 인덱스는 0번부터 N-1번까지)
        for change in range(L, R + 1):
            boxes[change] = i
    boxes = " ".join(map(str, boxes))
    print("#{} {}".format(tc, boxes))