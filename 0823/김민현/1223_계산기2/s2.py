import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    eq = input()

    s1,s2 = [],[]
    for i in eq:
        if '0'<= i <= '9': #아스키코드때문에 이렇게도 확인 가능
        #if i.isdecimal()도 사용 가능
            s1.append(int(i))
        else:
            if i =='+':
                while s2:
                    s1.append(s2.pop())
                s2.append(i)
            else:
                while s2 and s2[-1] == '*':
                    s1.append(s2.pop())
                s2.append(i)
    while s2:
        s1.append(s2.pop())


    for i in s1:
        if i == '+':
            num1 = s2.pop()
            num1 = s2.pop()
            s2.append(num1+num2)
        elif i == '*':
            num1 = s2.pop()
            num2 = s2.pop()
            s2.append(num1*num2)
        else:
            s2.append(i)
    print('#{} {}'.format(tc,s2[0]))





