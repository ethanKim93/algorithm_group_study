import sys
sys.stdin = open('sample_input.txt')

def pw(A, pk):
    code = {
        '0001101':'0',
        '0011001':'1',
        '0010011':'2',
        '0111101':'3',
        '0100011':'4',
        '0110001':'5',
        '0101111':'6',
        '0111011':'7',
        '0110111':'8',
        '0001011':'9'
    }
    pw = ''
    for i in range(0, 56*pk, 7*pk):
        temp = A[i:i+7]
        if temp in code:
            pw += code[temp]
        else:
            return
    # 잘 끝나면 pw 완성
    # pw 확인 절차
    add = test = 0
    for j in range(8):
        if j % 2:
            test += int(pw[j])
            add += int(pw[j])
        else:
            test += int(pw[j]) * 3
            add += int(pw[j])

    if test % 10 == 0:
        return pw

def code_sum(codes):
    result=0
    for code in codes:
        for i in range(8):
            result += int(code[i])
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lines = set()   # 한 줄씩/한 줄에 중복된 코드 있을 수 있음!
    codes = set()   # 암호 코드인 아이들의 set

    li = [input().strip('0') for _ in range(N)]
    for n in range(N):
        if li[n]:          # 빈 list가 아닐때
            temp = ''
            for i in range(len(li[n])):
                temp = bin(int(li[n],16))[2::].strip('0')
                lines.add(temp)

    for line in lines:
        pk = 1
        max_pk = len(line)//56 + 1
        while pk <= max_pk:
            hubo = line.zfill(56*pk)
            if pw(hubo,pk):
                codes.add(pw(hubo,pk))
            pk+=1

    end = code_sum(codes)
    print('#{} {}'.format(tc,end))

# 6번까지만 맞....ㅎㅎ...
