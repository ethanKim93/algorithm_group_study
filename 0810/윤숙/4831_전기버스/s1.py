import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    #K-> 한번 충전으로 최대한 이동할 수있는 정류장 수
    #N-> 종점
    #M-> 충전기가 설치된 정류장번호 갯수
    #M_n -> 충전기가 설치된 정류장번호
    #출력 노선번호 출력 횟구
    K,N,M=map(int,input().split())
    M_n=list(map(int,input().split()))

    Bus_Station=[0]*(N+1)
    Bus_charger=[0]*(N+1)
    for idx in range(0,len(Bus_Station),K):
        Bus_Station[idx]+=1
    Bus_charger[0]=1
    for idx in M_n:
        Bus_charger[idx]+=1
    print(Bus_Station)
    print(Bus_charger)