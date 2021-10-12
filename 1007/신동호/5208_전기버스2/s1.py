import sys
sys.stdin = open('sample_input.txt')

def bus(s): # 
    global cnt, M # 정차 횟수 cnt, 정류장에 대한 정보 M
    while s < M[0]: # 현재 버스 정류장이 마지막 버스 정류장 전일 때
        if not s + M[s] < M[0]: # 현재 버스 정류장에서 갈 수 있는 가장 먼 정류장이 마지막 버스 정류장 이상일 때
            return cnt # 정차 횟수 반환 
        max_d = 0 # 현재 버스 정류장에서 갈 수 있는 정류장 후보들의 가장 멀리 갈 수 있는 번호
        for i in range(1, M[s]+1): # 현재 버스 정류장에서 갈 수 있는 정류장 후보들을 모두 조회
            if max_d < s + i + M[s+i]: # max_d보다 정류장 후보에서 갈 수 있는 번호가 더 멂
                max_d = s + i + M[s+i] # max_를 정류장 후보에서 갈 수 있는 최대 번호로 교체
                before = s + i # 다음에 갈 정류장 후보 교체
        cnt += 1 # 정차 횟수 추가
        s = before # 다음에 갈 정류장 후보를 s에 저장

T = int(input())

for tc in range(1, T+1):
    M = list(map(int, input().split()))
    cnt = 0
    bus(1) # 1번 정류장에서 버스가 출발한다
    print('#{} {}'.format(tc, cnt))   
