import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int, input().split()) #최대이동K 도달거리N 충전소개수M
    station = list(map(int, input().split()))

    now = 0
    cnt = 0

    while now < N:
        now += K
        if now >= N: #끝에 도착하면 while 끝내고 cnt출력
            break
        for i in range(now, now-K, -1): #한 칸 되돌아가서
            if i in station: #충전기 있는지 확인
                now = i #충전기 있으면
                cnt += 1 #충전
                break
        else: #한칸씩 되돌아가 확인했는데 i가 station에 없음 하면 타는 분기
            cnt = 0 #몇 번 갔던걸 0으로 초기화(안 가면 계속0)
            break

    print('#{} {}'.format(tc, cnt))