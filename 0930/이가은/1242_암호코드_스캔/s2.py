# 보충 code

codes = {(3, 2, 1, 1): 0,
         (2, 2, 2, 1): 1,
         (2, 1, 2, 2): 2,
         (1, 4, 1, 1): 3,
         (1, 1, 3, 2): 4,
         (1, 2, 3, 1): 5,
         (1, 1, 1, 4): 6,
         (1, 3, 1, 2): 7,
         (1, 2, 1, 3): 8,
         (3, 1, 1, 2): 9
         }

hex_dic = {"0": [0, 0, 0, 0], "1": [0, 0, 0, 1], "2": [0, 0, 1, 0], "3": [0, 0, 1, 1], "4": [0, 1, 0, 0],
           "5": [0, 1, 0, 1],
           "6": [0, 1, 1, 0], "7": [0, 1, 1, 1], "8": [1, 0, 0, 0], "9": [1, 0, 0, 1], "A": [1, 0, 1, 0],
           "B": [1, 0, 1, 1], "C": [1, 1, 0, 0],
           "D": [1, 1, 0, 1], "E": [1, 1, 1, 0], "F": [1, 1, 1, 1]}

def solve(data):

    result = 0
    for i in range(N):
        j = M * 4 - 1  # 마지막 인덱스부터 검사
        while j >= 55:  # 암호의 길이가 56이니까
            if data[i][j] == 1 and data[i - 1][j] == 0:
                full_code = []
                for _ in range(8):
                    w1 = w2 = w3 = w4 = 0
                    while data[i][j] == 1:
                        w4 += 1
                        j -= 1
                    while data[i][j] == 0:
                        w3 += 1
                        j -= 1
                    while data[i][j] == 1:
                        w2 += 1
                        j -= 1
                    min_v = min(w2, w3, w4)
                    w2 //= min_v
                    w3 //= min_v
                    w4 //= min_v
                    w1 = 7 - w2 - w3 - w4

                    j -= w1 * min_v
                    full_code.append(codes[(w1, w2, w3, w4)])

                full_code.reverse()
                odd_sum = full_code[0] + full_code[2] + full_code[4] + full_code[6]
                even_sum = full_code[1] + full_code[3] + full_code[5] + full_code[7]
                if (odd_sum * 3 + even_sum) % 10 == 0:
                    result += odd_sum + even_sum

            else:
                j -= 1

    return result


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    arr = list()
    for i in range(N):
        tmp = list()
        for j in range(M):
            tmp += hex_dic[data[i][j]]
        arr.append(tmp)

    result = solve(arr)
    print("#{} {}".format(tc, result))