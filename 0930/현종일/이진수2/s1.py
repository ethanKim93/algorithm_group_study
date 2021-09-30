import sys
sys.stdin= open("sample_input.txt")

for tc in range(1, int(input())+1):
    n = float(input())
    n_2 = []
    divider = 0.5
    while n:
        if n >= divider:
            n_2.append('1')
            n -= divider
        else:
            n_2.append('0')
        divider /= 2
    print("#{} {}".format(tc, ''.join(n_2) if len(n_2) < 13 else "overflow"))

