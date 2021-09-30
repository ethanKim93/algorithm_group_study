import sys
sys.stdin = open('input.txt')
pwd = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}

# 암호코드의 첫번째 줄의 시작위치 또는 끝위치
def check_code():
    ans = 0
    # 행우선으로 순회(뒤에서 부터)
    for i in range(N): # i = 행
        j = M * 4 - 1
        while j >= 0:
            # 암호코드의 첫줄의 마지막 위치를 판단
            if arr[i][j] == 1 and arr[i - 1][j] == 0:
                # 8개의 패턴을 처리한다.
                read = []
                for _ in range(8):
                    c2 = c3 = c4 = 0
                    while arr[i][j] == 0: j -= 1
                    while arr[i][j] == 1: c4 += 1; j -= 1
                    while arr[i][j] == 0: c3 += 1; j -= 1
                    while arr[i][j] == 1: c2 += 1; j -= 1
                    # 최소 개수를 찾아서 key값 계산
                    min_cnt = min(c2, c3, c4)
                    read.append(pwd[(c2//min_cnt, c3//min_cnt, c4//min_cnt)])

                even = read[0] + read[2] + read[4] + read[6]
                odd = read[1] + read[3] + read[5] + read[7]
                if (odd * 3 + even) % 10 == 0:
                    ans += odd + even
            j -=1
    return ans

# 16진->2진
# 가변길이
# 다수 암호 중복처리
# 16진수 문자열 ==> 2진수 정수 리스트 [0, 0, 0, 1, 1, 0, ...]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]
    # 2진수 형태로 저장
    for i in range(N):
        tmp = input()
        for j in range(M):
            n = int(tmp[j], 16)
            arr[i].append(1 if n & 8 else 0)
            arr[i].append(1 if n & 4 else 0)
            arr[i].append(1 if n & 2 else 0)
            arr[i].append(1 if n & 1 else 0)

    print('#{} {}'.format(tc, check_code()))