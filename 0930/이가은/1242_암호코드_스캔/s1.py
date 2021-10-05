import sys
sys.stdin = open('sample_input.txt')

def change_bin(N):
    result = []

    if not(N.isdigit()):
        num = ord(N)-ord('A')+10
    else:
        num = int(N)

    for i in range(3, -1, -1):
        if num & (1 << i):
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)


def certification(data):
    test = add = 0
    result = False

    for i in range(8):
        if i % 2:
            test += int(data[i])
            add += int(data[i])
        else:
            test += int(data[i]) * 3
            add += int(data[i])

    if test % 10 == 0:
        result = add
    return result


def find_pw(arr):
    global result_pw

    codes = {
        (3, 2, 1, 1): 0,
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

    for m in range(4*M-1, -1, -1):
        tem = []

        for _ in range(8):
            if arr[m] =='1':
                b=c=d=0
                while arr[m] == '1':
                    d += 1
                    m -= 1
                while arr[m] == '0':
                    c += 1
                    m -= 1
                while arr[m] == '1':
                    b += 1
                    m -= 1

                min_v = min(b, c, d)
                b //= min_v
                c //= min_v
                d //= min_v
                a = 7 - b - c - d

                m -= a * min_v
                tem.append(codes[(a,b,c,d)])

            else:
                m -= 1
        print(tem)
        # if certification(tem) and tem not in result_pw:
        #         #     result_pw.append(tem)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    li = [input() for _ in range(N)]

    result_pw = []
    for i in range(N):
        password = ''
        if li[i] == [0]*M:
            pass
        else:
            for j in range(M-1,-1,-1):
                password += change_bin(li[i][j])
        find_pw(password)
    # print(result_pw)