import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    p = 1                               # 가로 길이가 N 일때의 경우의 수
    n = N//10                           # 범위 설정을 위한 N의 보정
    for i in range(1, n+1):
        if i%2:                         # i가 홀수 일때 이전 p값을 통한 경우의 수 갱신
            p = (p*2) - 1
        else:                           # i가 짝수 일때 이전 p값을 통한 경우의 수 갱신
            p = (p*2) + 1
    print('#{} {}'.format(tc, p))



# memoization
T = int(input())

Ns = []                                     # 입력되는 너비 값들을 담을 리스트
max_N = 0                                   # 너비 값의 최대값을 담을 변수 초기화
for _ in range(T):
    N = int(input())
    Ns.append(N//10)                        # 입력되는 너비 값을 보정해서 리스트에 추가
    if N//10 > max_N:                       # 입력되는 너비 값 중 최대값 저장
        max_N = N//10

memo = [1]                                  # 리스트의 마지막 항목을 기준으로 연산된 값을 기록하기 위한 초기화
for i in range(1, max_N):                   # 너비 최대값만큼 순회(그 이하의 너비에 대한 경우의 수는 아래에서 인덱스로 접근)
    if i%2:                                 # 홀수 회차인 경우 연산 후 값을 추가
        memo.append(memo[i-1]*2 + 1)
    else:                                   # 짝수 회차인 경우 연산 후 값을 추가
        memo.append(memo[i-1]*2 - 1)

for idx, j in enumerate(Ns):                # Ns 리스트에 할당된 각 value가 memo 리스트의 key로 존재하므로 이를 통해 접근하여 출력
    print('#{} {}'.format(idx+1, memo[j-1]))