import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1,t+1):
    n = float(input())
    temps = ""
    cnt = 0
    ans = 'okay'
    while n != 0.0:
        n *= 2
        temps += str(int(n))
        n -= int(n)
        cnt += 1

        if cnt == 13:
            ans = 'overflow'
            break

    print("#" + str(tc), end=" ")
    print(temps) if ans =="okay" else print(ans)