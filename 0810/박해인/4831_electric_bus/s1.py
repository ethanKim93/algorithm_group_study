import sys
sys.stdin = open("sample_input.txt")

T = int(input()) # 노선 수
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N 종점
    # M 충전기가 설치된 정류장
    charger = list(map(int, input().split()))

    max_distance = [0] + K
    if N < max_distance:


    for i in


