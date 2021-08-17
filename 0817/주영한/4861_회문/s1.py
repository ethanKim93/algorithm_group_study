import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [0] * N
    for i in range(N):
        matrix[i] = input()

    flag = False
    result = 0

    # 가로축 점검
    for row in range(N):
        if flag:
            break
        for col in range(N - M + 1):
            temp_text = matrix[row][col:col+M]
            if temp_text == temp_text[::-1]:
                flag = True
                result = temp_text
                break

    # 세로축 점검
    for col in range(N):
        if flag:
            break
        for row in range(N - M + 1):
            temp_text = []
            for k in range(M):
                temp_text.append(matrix[row + k][col])
            temp_text = "".join(temp_text)
            if temp_text == temp_text[::-1]:
                flag = True
                result = temp_text
                break

    print("#{} {}".format(tc, result))
