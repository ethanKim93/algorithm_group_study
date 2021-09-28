import sys
sys.stdin = open('input.txt')

# 가로
def hori():
    result = 0
    for i in range(9):
        nums = list(range(1, 10))
        cnt = 0
        for j in range(9):
            if arr[i][j] in nums:
                nums.remove(arr[i][j])
                cnt += 1
            else:
                return False
        if cnt == 9:
            result += 1
    if result == 9:
        return True
    return False


#세로
def vert():
    result = 0
    for i in range(9):
        nums = list(range(1, 10))
        cnt = 0
        for j in range(9):
            if arr[j][i] in nums:
                nums.remove(arr[j][i])
                cnt += 1
            else:
                return False
        if cnt == 9:
            result += 1
    if result == 9:
        return True
    return False


# 3 * 3
def third():
    result = 0
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            nums = list(range(1, 10))
            cnt = 0
            for x in range(3):
                for y in range(3):
                    if arr[i+x][j+y] in nums:
                        nums.remove(arr[i+x][j+y])
                        cnt += 1
            if cnt == 9:
                result += 1
    if result == 9:
        return True
    return False


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if hori() and vert() and third():
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))