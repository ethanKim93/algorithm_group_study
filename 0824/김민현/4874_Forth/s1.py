import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    eq = list(input().split())
    s1 = []
    for i in eq:
        if '0' <= i <='9':
            s1.append(int(i))
        elif i =='.':
            if len(result) == 1:
                print('#{} {}'.format(tc,s1[0]))
                break
            else:
                print('#{} error'.format(tc))
                break
        elif len(s1)>=2:
            a = s1.pop()
            b = s1.pop()
            if i == '+':
                s1.append(a + b)
            elif i =='-':
                s1.append(a - b)
            elif i == '*':
                s1.append(a * b)
            elif i == '/':
                s1.append(a // b)
        else:
            print('#{} error'.format(tc))
            break

