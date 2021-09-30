import sys
sys.stdin = open('input.txt')
pattern = ['0001101',
           '0011001',
           '0010011',
           '0111101',
           '0100011',
           '0110001',
           '0101111',
           '0111011',
           '0110111',
           '0001011',
           ]
# 마지막 인덱스에서 시작해서 1을 찾으면 해당 열에서 55를 뺀 패턴의 시작 인덱스 반환
def find_st(N, M):
    for i in range(N):
        for j in range(M-1, 54, -1):
            if arr[i][j] == '1':
                return i, j-55
# 첫번째 패턴의 인덱스를 찾고 패턴을 비교하여 10으로 나눠지면 더한 값 반환
def verif(N, M):
    i, j = find_st(N, M)
    pwd = []
    while len(pwd) < 8:
        for k in range(10):
            if pattern[k] == arr[i][j:j+7]:
                pwd.append(k)
                j+=7
    ans = 0
    if not ((pwd[0]+pwd[2]+pwd[4]+pwd[6])*3 + pwd[1] + pwd[3] + pwd[5] + pwd[7])%10:
        for p in pwd:
            ans += p
    return ans
    
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print('#{} {}'.format(tc, verif(N, M)))
