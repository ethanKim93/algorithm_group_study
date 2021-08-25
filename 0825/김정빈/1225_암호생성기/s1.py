import sys
sys.stdin = open("input.txt")

def password(pw):
    while pw[-1] > 0:
        for i in range(1, 6):
            cg = pw.pop(0)
            if cg - i <= 0:
                pw.append(0)
                break
            else:
                pw.append(cg - i)
    return pw

for _ in range(1, 11):
    tc = int(input())
    pw = list(map(int, input().split()))

    print('#{} '.format(tc), end="")
    print(*password(pw))