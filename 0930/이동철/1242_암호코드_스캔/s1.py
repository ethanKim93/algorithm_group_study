import sys
sys.stdin = open('sample_input.txt', 'r')

# 2진수 dict
binary = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

# 암호코드 dict
code = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
    (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9,
}

T = int(input())
for tc in range(1, T + 1):
    # N = 세로, M = 가로
    N, M = map(int, input().split())

    # 중복 제거, 0만 있는 배열 제거
    arr = sorted(list(set([input()[:M] for _ in range(N)])))

    last = 0
    visited = []
    arr.pop(0)

    # 2진수 변환
    for i in range(len(arr)):
        result = ''
        for j in range(len(arr[i])):
            result += binary[arr[i][j]]
        
        # result 의 오른쪽 0 제거
        result = result.rstrip('0')
        
        # 0, 1을 이용해서 숫자 찾기
        ze_one = []

        n1 = n2 = n3 = n4 = 0
        for k in range(len(result)-1, -1, -1):
            if result[i] == '1' and n3 == 0:
                n4 += 1
            elif result[i]
