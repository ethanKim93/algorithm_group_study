import sys
sys.stdin = open('input.txt')



T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    code_key = []
    for i in range(N):
        secret = input()
        if secret == '0'*M:continue
        else:
            k = M-1
            while k > 14:
                if secret[k] != '0':
                    ratio = 1
                    while True:
                        a= secret[k]
                        b= secret[k - ((14 * ratio))]
                        c = 0
                        if secret[k-((14*ratio)+1)] =='0':
                            break
                        else:
                            ratio += 1
                    if secret[k-((14*ratio)):k+1] not in code_key:
                        code_key.append(secret[k-((14*ratio)):k+1])
                        a = 1
                    k -= 14*ratio
                k -= 1

    pattern = {
        '0'*3*ratio+'1'*2*ratio+'0'*1*ratio+'1'*1*ratio: 0,
        '0'*2*ratio+'1'*2*ratio+'0'*2*ratio+'1'*1*ratio: 1,
        '0'*2*ratio+'1'*1*ratio+'0'*2*ratio+'1'*2*ratio: 2,
        '0'*1*ratio+'1'*4*ratio+'0'*1*ratio+'1'*1*ratio: 3,
        '0'*1*ratio+'1'*1*ratio+'0'*3*ratio+'1'*2*ratio: 4,
        '0'*1*ratio+'1'*2*ratio+'0'*3*ratio+'1'*1*ratio: 5,
        '0'*1*ratio+'1'*1*ratio+'0'*1*ratio+'1'*4*ratio: 6,
        '0'*1*ratio+'1'*3*ratio+'0'*1*ratio+'1'*2*ratio: 7,
        '0'*1*ratio+'1'*2*ratio+'0'*1*ratio+'1'*3*ratio: 8,
        '0'*3*ratio+'1'*1*ratio+'0'*1*ratio+'1'*2*ratio: 9
    }
    #print(pattern)
    for code in code_key:
        binary = ''
        for c in code:
            for i in range(3,-1,-1):
                binary += '1' if int(c,16) & (1<<i) else "0"
        print(binary)
        for i in range(len(binary)-1,-1,-1):
            print(i)
            if binary[i] == '1':
                if i == len(binary)-1:
                    binary = binary[i-(56*ratio-1):i]

                else:
                    binary = binary[i-(56*ratio-1):i]
                    break
        #print(binary)
        temp = []
        ans = 0
        print(code)
        print(binary)
        while len(binary) > 0:
            temp.append(pattern[binary[:7*ratio]])
            binary = binary[7*ratio:]

        total_a = 0
        total_b = 0
        print(temp)
        for m in range(7):
            if m%2:
                total_b += temp[m]
            else:
                total_a += temp[m]
        total = (total_a)*3 +total_b +temp[7]
        if not total%10:
            ans = sum(temp)
            break
    print('#{} {}'.format(tc,ans))