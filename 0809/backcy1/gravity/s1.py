import sys
sys.stdin = open('input.txt')

# Gravity
T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 가로, 세로
    room = [[0] * M for _ in range(N)]    # 방 넓이
    H = list(map(int, input().split()))  # N개의 상자들이 쌓여 있는 높이
    result = 0                            # 낙차가 가장 큰 값

    for i in range(N):                    # 방에 상자 쌓기(1로 표현)
      for j in range(H[i]):
        room[i][j] = 1

    # 각 상자의 낙차 구하기
    for i in range(N):  # 가로
      for j in range(M):  # 세로
        if room[i][j] == 1:  # 박스일 때
          max_value = 0
          for k in range(i + 1, N):   # 가로
            if room[k][j] == 0:       # 박스가 없으면 낙차 1 증가
              max_value += 1
          if result < max_value:
            result = max_value

    print(result)
