import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    d, m1, m3, y = map(int, input().split())
    maps = [0] + list(map(int,input().split()))
    temps = [0] * 13
    temps[1] = min(d*maps[1], m1)
    temps[2] = temps[1] + min(d*maps[2], m1)
    for i in range(3,13):
        temps[i] = min(temps[i-3]+m3, temps[i-1]+m1, temps[i-1]+d*maps[i])

    ans = min(y, temps[12])
    print("#{} {}".format(tc,ans))

# Pass