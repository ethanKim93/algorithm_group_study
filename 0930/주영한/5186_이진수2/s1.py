ERR = 1E-9

def to_binary(float_num):
    result = ""
    cnt = -1
    while not -ERR < float_num < ERR:
        if cnt == -13:
            return "overflow"
        if float_num >= 2 ** cnt:
            result += '1'
            float_num -= 2 ** cnt
        else:
            result += '0'
        cnt -= 1
    return result

for tc in range(1, int(input()) + 1):
    target = float(input())
    print("#{} {}".format(tc, to_binary(target)))
