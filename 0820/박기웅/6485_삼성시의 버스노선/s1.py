import sys
sys.stdin = open("s_input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
        
    C = [] # 버정 
    P = int(input()) # 버정 수
    cnt = [0]*5001 # count 배열 정의1<=C<=5000 이므로5001개 정의
    for _ in range(P):
        C.append(int(input()))

    #정류장 지나는 노선 개수 누적
    for ab in AB: 
        for i in range(ab[0], ab[1]+1):
            cnt[i] += 1

    # 출력
    ans = []
    for c in C:
        ans.append(cnt[c])
    print('#{} {}'.format(tc, ' '.join(map(str, ans))))
