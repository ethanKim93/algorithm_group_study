import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    text = []
    for i in range(5):
        text.append(input())

    temps = [["no"]*15 for _ in range(5)]

    for i in range(5):
        for x in range(len(text[i])):
            temps[i][x] = text[i][x]

    ans = ""
    for i in range(15):
        for x in range(5):
            if temps[x][i] != "no":
                ans += temps[x][i]
    print("#{} {}".format(tc,ans))