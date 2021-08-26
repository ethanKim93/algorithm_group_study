import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    pizza = list(map(int, input().split()))
    q = [[] for _ in range(N)]                  # 화덕 사이즈에 맞는 queue 생성
    for i in range(N):
        q[i] = [i+1, pizza[i]]                  # 화덕에 피자 번호와 함께 피자 투입

    a = 0
    while len(q) > 1:
        idx, cheese = q.pop(0)                  # 1번 위치에서 꺼내서
        cheese //= 2                            # 치즈를 반감시키고
        if cheese:                              # 치즈가 아직 남아있는 경우
            q.append([idx, cheese])             # 그대로 화덕에 투입
        else:                                   # 치즈가 다 녹아서 남아있는 피자가 추가 투입하는 경우
            if a < M-N:                         # N+a+1번째 피자가 있으면 화덕에 투입
                q.append([N+a+1, pizza[N+a]])
                a += 1                          # a 를 1 증가해서 남은 피자 여부 확인할 수 있도록 수정
    print('#{} {}'.format(tc, q[0][0]))