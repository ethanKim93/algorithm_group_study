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
                a = total.pop(-2)   # 분자 분모!
                b = total.pop()
                c = int(a) // int(b)
                total.append(c)

            elif i == '-':      # 빼는 순서!
                a = total.pop(-2)
                b = total.pop()
                c = int(a) - int(b)
                total.append(c)

            elif i == '.':
                if len(total) > 1:  # '.'이 나왔는데 최종적으로 append 된 값 말고 더 올라와있으면 계산 불가 하니까
                    print('#{} {}'.format(tc, 'error'))  # error 반환
                else:
                    print('#{} {}'.format(tc, total[0]))

            else:
                total.append(i)
    except:
        print('#{} {}'.format(tc, "error"))





