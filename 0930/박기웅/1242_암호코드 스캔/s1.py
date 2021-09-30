import sys
sys.stdin = open('sample_input.txt')

# hexa = {}
# for i, h in enumerate('0123456789ABCDEF'):
#     hexa[h] = i

rate = {211:0,
        221:1,
        122:2,
        411:3,
        132:4,
        231:5,
        114:6,
        312:7,
        213:8,
        112:9,
       }

# 마지막 패턴의 끝에서 시작해서 i 행으로 내려서 0을 만날 때까지 지움
def erase(i, j, rt):
    st = i
    while arr[st][j] == 1:
        st += 1
    for r in range(i, st):
        for c in range(j-56*rt+1, j+1):
            arr[r][c] = 0

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ans = 0
    # 16진수 -> 2진수 4자리로 저장
    arr = []
    for _ in range(N):
        bins = []
        for i in input():
            a = int(i, 16)                 # 10진수로 형변환
            for j in range(3, -1, -1):    # 비트연산을 통해 4자리 2진수로 변경
                bins.append(1 if a & (1<<j) else 0)
        arr.append(bins)
    # 열이 4배로 늘어남
    M *= 4 
    for i in range(N):
        j = M-1
        p = last = 0    # 찾은 암호 숫자의 개수, 마지막 패턴의 끝 인덱스
        pwd = [0]*8     # 암호패턴 8개
        while j>=0:
            if arr[i][j]:
                if not p: last = j  # p가 0일 때의 인덱스
                cnt = [0]*3     # 패턴과 비교할 리스트
                pat = [1, 0, 1] # 1 찾고 -> 0 찾고 -> 1찾고
                for k in range(3):
                    while arr[i][j] == pat[k]:
                        cnt[2-k] += 1
                        j -= 1
                rt = min(cnt)                # r = 비율
                cnt = [c//rt for c in cnt]
                pwd[7-p] = rate[cnt[0]*100+cnt[1]*10+cnt[2]]
                p += 1
                if p == 8:
                    if not ((pwd[0]+pwd[2]+pwd[4]+pwd[6])*3 + pwd[1] + pwd[3] + pwd[5] + pwd[7])%10:
                        ans += sum(pwd)
                    erase(i, last, rt)
                    # p = 0
            else:
                j -= 1
    print('#{} {}'.format(tc, ans))