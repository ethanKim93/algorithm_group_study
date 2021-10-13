import sys
sys.stdin = open('input.txt')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


def calc(n):
    idx = 0
    while n and idx < 8:                # 1의자리 수가 0이 아닌 케이스가 있으므로 8번째에 멈추도록 idx<8 설정
        tmp = n // money[idx]           # 5만원부터 순서대로 최대 몇 개를 줄 수 있는지 tmp에 저장
        n -= tmp * money[idx]           # 잔돈에서 해당 금액만큼 차감
        ans[idx] = tmp                  # ans에 현재 화폐 몇 개 사용했는지 저장
        idx += 1                        # 다음 화폐로 넘어가기


T = int(input())
for tc in range(1, T+1):
    change = int(input())               # 잔돈 입력받기
    ans = [0] * 8                       # 각 화폐를 몇 개 사용했는지 저장할 배열
    calc(change)                        # 계산
    print('#{}'.format(tc))             # 출력
    print(' '.join(map(str, ans)))