import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    text = list(input().split())

    total = []

    try:
        for i in text:
            if i == '+':
                a = total.pop()
                b = total.pop()
                c = int(a) + int(b)
                total.append(c)

            elif i == '*':
                a = total.pop()
                b = total.pop()
                c = int(a) * int(b)
                total.append(c)

            elif i == '/':
                a = total.pop(-2)
                b = total.pop()
                c = int(a) // int(b)
                total.append(c)

            elif i == '-':
                a = total.pop(-2)
                b = total.pop()
                c = int(a) - int(b)
                total.append(c)

            elif i == '.':
                if len(total) > 1:
                    print('#{} {}'.format(tc, 'error'))
                else:
                    print('#{} {}'.format(tc, total[0]))

            else:
                total.append(i)
    except:
        print('#{} {}'.format(tc, "error"))





