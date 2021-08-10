import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for j in range(0, T):
    KNM = list(map(int, input().split()))   # K N M을 각각 나눠서 리스트에 저장 / KNM[0]은 버스 이동량, 1은 종점 위치, 2는 충전기 갯수
    M = list(map(int, input().split())) + [KNM[1]]  # 종점 위치를 확인하기 위해 설치된 충전기 위치 리스트의 마지막에 종점 위치를 추가

    cnt = 0 # 이동횟수
    bus = 0 # 버스위치

    for i in range(KNM[2]+1):
        if bus + KNM[0] >= KNM[1]:  # 버스 위치가 종점을 지나면 종료
            break
        else:
            if bus + KNM[0] == M[i]:  # 버스 도착 위치가 충전소 위치일 경우
                cnt += 1              # cnt에 1을 더하고 버스 위치를 현재 충전소 위치로 변경
                bus = M[i]
            elif bus + KNM[0] < M[i]:   # 버스 도착 위치가 충전소 위치가 아닐 경우
                if M[i-1] + KNM[0] > M[i]: # 이전 충전소에서 버스 이동량만큼 간 위치가 현재 충전소보다 크다면
                    cnt += 1                # cnt에 1을 더하고 버스 위치를 현재 충전소 위치로 변경
                    bus = M[i-1]
                else:   # 이전 충전소에서 버스 이동량만큼 간 위치가 현재 충전소보다 작다면
                    cnt = 0     # 충전기에 도달하지 못했기에 0으로 변환 및 종료
                    break

    print('#{} {}'.format(j+1, cnt))