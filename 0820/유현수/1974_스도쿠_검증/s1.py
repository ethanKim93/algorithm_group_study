import sys
sys.stdin = open('input.txt')


def rc_check(sdk):
    for i in range(9):
        stack_r = []
        stack_c = []
        for j in range(9):
            if not stack_r:
                stack_r.append(sdk[i][j])
            else:
                if sdk[i][j] in stack_r:
                    return 0
                else:
                    stack_r.append(sdk[i][j])

            if not stack_c:
                stack_c.append(sdk[j][i])
            else:
                if sdk[j][i] in stack_c:
                    return 0
                else:
                    stack_c.append(sdk[j][i])
    return 1


def box_check(sdk):
    for i in range(3):
        for j in range(3):
            stack = []
            for k in range(3):
                for l in range(3):
                    if not stack:
                        stack.append(sdk[i*3+k][j*3+l])
                    else:
                        if sdk[i*3+k][j*3+l] in stack:
                            return 0
                        else:
                            stack.append(sdk[i * 3 + k][j * 3 + l])
    return 1


T = int(input())
for tc in range(1, T+1):
    sdk = [list(map(int, input().split())) for _ in range(9)]

    result = rc_check(sdk) and box_check(sdk)
    print('#{} {}'.format(tc, result))
