import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    print(1)                                    # 일단 1은 항상 출력

    temp = []
    for i in range(N-1):                        # N이 2보다 큰 경우 반복
        now = [1]                               # 1로 시작하는 리스트 초기화
        for j in range(i):                      # i 범위 만큼 반복하며
            now.append(temp[j] + temp[j+1])     # 왼쪽과 오른쪽 위 숫자의 합을 추가
        now.append(1)                           # 마지막에 1을 추가
        print(*now)
        temp = now                              # 위에서 만든 리스트를 temp 변수에 저장 후 다음 반복문에서 활용
