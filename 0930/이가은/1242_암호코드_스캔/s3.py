import sys
sys.stdin = open('sample_input.txt')

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

def pw(A, pk):
    rip = ''
    for i in range(0, 8):
        temp = A[i*7*pk : (i+1)*7*pk : pk]
        if temp in code:
            rip += code[temp]
        else:
            return
    return rip
    # 잘 끝나면 rip 완성
    # rip 확인 절차

def code_sum(codes):
    total = 0
    for code in codes:
        test = result = 0
        for j in range(8):
            if j%2:
                test += int(code[j])
                result += int(code[j])
            else:
                test += int(code[j])*3
                result += int(code[j])
        if test%10 ==0:
            total += result
    return total

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lines = set()   # 한 줄씩/한 줄에 중복된 코드 있을 수 있음!
    codes = set()   # 암호 코드인 아이들의 set

    li = [input().strip('0') for _ in range(N)]
    for n in range(N):
        if li[n]:          # 빈 list가 아닐때
            for i in range(len(li[n])):
                lines.add(bin(int(li[n],16))[2::].strip('0'))
    # print(*lines,sep='\n')

    for line in lines:
        pk = 1
        max_pk = len(line)//56 + 1
        while pk <= max_pk:
            line = line.zfill(56*pk)
            hubo = line[-56*pk:]

            if pw(hubo,pk):
                codes.add(pw(hubo,pk))
                line = line[:-56*pk].rstrip('0')
                pk = 1
            else:
                pk += 1

    end = code_sum(codes)
    print('#{} {}'.format(tc,end))