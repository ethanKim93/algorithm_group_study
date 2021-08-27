import sys
sys.stdin = open("input.txt")

def transpose(matrix):
    L = len(matrix)
    for row in range(L):
        for col in range(row, L):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

for tc in range(1, 11):
    dummy = input()
    magentic_field = [list(map(int, input().split())) for _ in range(100)]

    # 전치행렬을 활용하여 비교에 용이하게 바꾼다.
    transpose(magentic_field)

    result = 0

    for col_field in magentic_field:
        # 이전값을 저장할 임시 변수 지정
        magetic_buffer = 0
        for row in col_field:
            if row:
                # 임시 변수가 1이고, 현재 확인하는 값이 2일 경우, 교착상태이므로
                # 카운트해준다.
                if magetic_buffer == 1 and row == 2:
                    result += 1
                # 이후 임시 변수를 업데이트 한다
                magetic_buffer = row

    print("#{} {}".format(tc, result))