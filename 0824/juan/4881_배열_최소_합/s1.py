T = int(input())

def powerset(idx, temp):                                        # 현재 확인하고있는 행 번호(idx), 해당 행에서 선택한 값까지 더한 중간 합(temp)
    global result
    if temp > result:                                           # 현재까지의 합이 지금까지 알고있는 배열 최소 합(result)보다 크면 더이상 볼 필요 없으니 return
        return
    if idx == N:                                                # 마지막 행의 값까지 더한 경우
        if temp < result:                                       # 현재의 합이 배열 최소 합보다 작으면 교체
            result = temp
    for i in range(N):                                          # N만큼 순회
        if not use[i]:                                          # 아직 사용하지 않은 열이라면
            use[i] = 1                                          # 사용하고
            powerset(idx+1, temp+arr[idx][i])                   # powerset 함수 재귀호출하면서 idx값 증가시켜서 다음행 확인 및 현재까지의 배열 합도 인자로 넘김
            use[i] = 0                                          # 13번줄에서 호출한 powerset 함수가 return 된 경우 마지막으로 사용처리했던 열은 다시 미사용 처리하고 함수 종료
                                                                # 그래야 for문에 의한 i의 증가로 방금 선택했던 순열이 아닌 다음 순열에 해당하는 인덱스 선택이 가능

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 입력
    result, temp = 100, 0                                       # 배열 최소 합(result), 배열 최소 합과 비교할 임시 합(temp)
    use = [0] * N                                               # 사용한 열(column)을 기록하기 위한 리스트

    powerset(0, 0)
    print('#{} {}'.format(tc, result))