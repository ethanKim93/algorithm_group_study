import sys
sys.stdin = open('input.txt')

pattern = {(2, 1, 1): 0,
           (2, 2, 1): 1,
           (1, 2, 2): 2,
           (4, 1, 1): 3,
           (1, 3, 2): 4,
           (2, 3, 1): 5,
           (1, 1, 4): 6,
           (3, 1, 2): 7,
           (2, 1, 3): 8,
           (1, 1, 2): 9}

hexTobin = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1,], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1], '4': [0, 1, 0, 0],
            '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1], '8': [1, 0, 0, 0,],
            '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
            'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}

def find():
    ans = 0
    for i in range(N):
        idx = M * 4 - 1 # 2진수로 만든 리스트를 뒤에서 부터 세기 위해

        while idx >= 55:
            if arr[i][idx] and arr[i-1][idx] == 0: # 한줄만 하기 위해

                pwd = []
                for _ in range(8):
                    # 뒤에서부터 1 카운트 0카운트 1카운트를 각각 c4 c3 c2에 저장함.
                    # 코드의 패턴을 보면 맨뒤가 1 다음이 0 다음이 1 순으로 되어 있음
                    c2 = c3 = c4 = 0
                    #처음 나오는 0들을 버리자.
                    while arr[i][idx] == 0: idx -= 1
                    while arr[i][idx] == 1: c4, idx = c4 + 1 , idx - 1 # 1을 만났으면 1을 카운트
                    while arr[i][idx] == 0: c3, idx = c3 + 1 , idx - 1 # 0을 만났으면 카운팅
                    while arr[i][idx] == 1: c2, idx = c2 + 1 , idx - 1 # 1을 만났으면 카운팅
                    min_value = min(c2, c3, c4)
                    pwd.append(pattern[(c2//min_value, c3//min_value, c4//min_value)])

                b = pwd[0] + pwd[2] + pwd[4] + pwd[6] # 짝수번째 자리
                a = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                if (a*3+b) % 10 == 0:
                    ans += a+b

                return ans
            idx -= 1




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hexTobin[tmp[j]]
        #전부 2진수로 바꿈

    print("#{} {}".format(tc, find()))


