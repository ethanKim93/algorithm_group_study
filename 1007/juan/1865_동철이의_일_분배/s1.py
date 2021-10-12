import sys
sys.stdin = open('input.txt')


def success(idx, percent):
    global best
    if idx == N:
        best = percent                                  # idx가 N에 도달하면 현재 최대 성공률 갱신
    else:
        if percent <= best:                             # 중간에 이미 현재 최대 성공률보다 성공률이 낮아지면 가능성이 없으므로 가지치기
            return
        for i in range(idx, N):
            used[idx], used[i] = used[i], used[idx]     # 성공률 교환
            now = percent * ability[idx][used[idx]]     # 현재의 성공률 연산
            if now > best:                              # 현재 성공률이 현재 최대 성공률보다 높은 경우에만 함수 재귀 호출
                success(idx+1, now)
            used[idx], used[i] = used[i], used[idx]     # 성공률 원상태 복원


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 입력되는 성공률 정보 백분율로 변환해서 저장
    ability = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    used = [i for i in range(N)]                        # 업무 번호 배열
    best = 0
    success(0, 1)

    print('#{} {:.6f}'.format(tc, best*100))