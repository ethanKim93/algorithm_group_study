# -*- coding: utf-8 -*-

T = int(input())


def bactrackin(pos, temp_result):
    global N, height, result

    # 만약 전부 다 확인 했을 경우,
    # 비교하여할 높이보다 현재 확인하는 경우의 높이가 크고, result로 기존에 저장된 상태보다 작을 경우
    # 값을 업데이트한다.
    if pos == N:
        if result > temp_result >= height:
            result = temp_result
        return

    # 키를 비교하다가 현재 확인하는 경우의 높이가 result로 기존에 저장된 상태보다 큰 경우,
    # 더 이상 볼 필요가 없다 (최소 차를 구해야 하므로)
    if result < temp_result:
        return
    
    # 해당하는 pos 인덱스의 직원이 포함 되었을 경우와 이닌 경우에 대한 재귀 함수 호출
    bactrackin(pos + 1, temp_result + height_set[pos])
    bactrackin(pos + 1, temp_result)    
    return 


for tc in range(1, T + 1):
    # 직원의 수와 비교하여야할 높이에 대한 변수 정의
    N, height = map(int, input().split())
    
    # 직원들의 키를 저장하는 변수 정의
    height_set = list(map(int, input().split()))

    # 최대 키 10000 / 최대 명수 20명이므로 최대로 발생 할 수 있는 경우보다 큰 값을 결과값에 초기화
    result = 10000 * 21
    
    # 백트래킹 실시
    bactrackin(0, 0)
    print("#{} {}".format(tc, result - height))
