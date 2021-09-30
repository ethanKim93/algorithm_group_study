import sys
sys.stdin = open('input.txt')

code = {
    '1011000': 0, '1001100': 1,                                 # 검증코드를 거꾸로 저장
    '1100100': 2, '1011110': 3,
    '1100010': 4, '1000110': 5,
    '1111010': 6, '1101110': 7,
    '1110110': 8, '1101000': 9
}


def search_start(a_str):                                        # 거꾸로 문자를 받아 탐색하며 1로시작하는 시작점을 찾는 함수
    for j in range(0, len(a_str)):
        if a_str[j] == '1':
            for code_pattern in code.keys():
                if code_pattern == a_str[j:j + 7]:
                    point = j
                    return point
    return -1                                                   # 끝까지 탐색 했지만 검증코드와 맞지 않으면 -1 반환


def analysis_code(col, code_str):                               # 문자를 검증코드를 통해 해석하는 함수
    res = []
    for k in range(col, M, 7):
        res.append(int(code.get(code_str[k:k + 7])))
        if len(res) == 8:                                      # 결과값이 8개가 되면 반환
            return res[::-1]
    return None                                                # 결과값이 8개가 안되면 해석불가


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code_map = [list(input().split()) for _ in range(N)]
    start_col = -1
    start_raw = -1
    ans_nominee = 0

    for i in range(N):                                         # 행 탐색
        start_col = search_start(code_map[i][0][::-1])
        start_raw = i
        if not start_col == -1:
            start_map = code_map[start_raw]
            code_nominee = analysis_code(start_col, start_map[0][::-1])
            ans_nominee = (code_nominee[0]+code_nominee[2]+code_nominee[4]+code_nominee[6]) * 3 + \
                (code_nominee[1]+code_nominee[3]+code_nominee[5]) + code_nominee[7]

            if not ans_nominee % 10:
                print('#{} {}'.format(tc, sum(code_nominee)))
                break
    if ans_nominee % 10:                                        # 테스트케이스 모든 행을 탐색 했지만 답을 못찾은 경우
        print('#{} {}'.format(tc, 0))
