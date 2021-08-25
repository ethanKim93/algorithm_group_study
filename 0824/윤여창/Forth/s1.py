import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    eq = list(input().split())
    s1 = []
    for i in eq:
        if '0' <= i <='9': #숫자 확인
            s1.append(int(i))
        elif i =='.': #.일 경우
            if len(s1) == 1: #.일때 길이가 1이면 값 출력, 아닐경우 error 발생
                print('#{} {}'.format(tc,s1[0]))
                break
            else:
                print('#{} error'.format(tc))
                break
        elif len(s1)>=2:
            a = s1.pop()
            b = s1.pop()
            if i == '+':
                s1.append(b + a)
            elif i =='-':
                s1.append(b - a)
            elif i == '*':
                s1.append(b * a)
            elif i == '/':
                s1.append(b // a)
        else:
            print('#{} error'.format(tc))
            break

