import sys
sys.stdin = open('input.txt')

password = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4, "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}
def striper(s):
    s = s.strip('0')
    return s
T = int(input())
for tc in range(1,T+1):
    answer = 0
    codes = []
    N,M = map(int,input().split())
    cal_datas = sorted(list(set([input() for _ in range(N)])))
    del cal_datas[0]
    for cal_data in cal_datas:
        cal_data = striper(cal_data)
        data = ''
        for i in cal_data:
            data += bin(int(i, 16))[2:].zfill(4)
        k = 0
        while len(data)>=56:
            data = '000'+data.rstrip('0')
            k += 1
            test_data = data[-56*k:]
            test_data = test_data[::k]

            try: # 해보고
                code = []
                for j in range(0,56,7):
                    code.append(password[test_data[j:j+7]])
                check = (code[0]+code[2]+code[4]+code[6])*3+code[1]+code[3]+code[5]+code[7]
                if check%10:
                    pass
                else:
                    if (k,code) in codes:
                        pass
                    else:
                        codes.append((k,code))
                        answer += sum(code)
                data = test_data[:-56 * k + 1].rstrip('0')
            except: # 실패하면
                continue
    print(answer)





