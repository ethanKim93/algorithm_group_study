import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    ope_li = list(map(str, input().split()))

    i = 0
    result = []
    flag = True

    while i < len(ope_li)-1:
        try:
            if ope_li[i] == '+':
                a = result.pop()
                b = result.pop()
                result.append(a+b)
            elif ope_li[i] == '-':
                a = result.pop()
                b = result.pop()
                result.append(b-a)
            elif ope_li[i] == '*':
                a = result.pop()
                b = result.pop()
                result.append(a*b)
            elif ope_li[i] == '/':
                a = result.pop()
                b = result.pop()
                result.append(b//a)
            else:
                result.append(int(ope_li[i]))
        except:
            flag = False
            break
        i += 1

    if len(result) == 1 and flag:
        print('#{} '.format(tc+1), end='')
        print(*result)
    else:
        print('#{} error'.format(tc+1))

