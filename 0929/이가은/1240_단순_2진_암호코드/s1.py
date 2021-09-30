import sys
sys.stdin = open('input.txt')

T = int(input())

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

for tc in range(1, T+1):
    N, M = map(int, input().split())

    li = list(input() for _ in range(N))

    cnt = 0
    for n in range(N):
        if li[n] == '0'*M:
            pass
        else:
            for m in range(M-1,-1,-1):
                if li[n][m] == '1':
                    word = li[n][m-55:m+1]
                    cnt += 1
                    break

    result = 0
    if cnt > 4:
        pw=''
        for i in range(0,56,7):
            temp = word[i:i+7]
            pw += code[temp]

        test =0
        add = 0
        for j in range(8):
            if j%2:
                test += int(pw[j])
                add += int(pw[j])
            else:
                test += int(pw[j])*3
                add += int(pw[j])

        if test%10==0:
            result=add

    print('#{} {}'.format(tc, result))

