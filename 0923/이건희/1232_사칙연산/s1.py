import sys
sys.stdin = open("input.txt")

def postorder(l):
    global values
    if type(values[l]) == str:
        if values[l] == "+":
            values[l] = postorder(temps1[l]) + postorder(temps2[l])
        elif values[l] == "-":
            values[l] = postorder(temps1[l]) - postorder(temps2[l])
        elif values[l] == "*":
            values[l] = postorder(temps1[l]) * postorder(temps2[l])
        else:
            values[l] = postorder(temps1[l]) / postorder(temps2[l])
        return values[l]
    else:
        return values[l]


for tc in range(1, 11):
    n = int(input())
    values = [0] * (n + 1)
    temps1 = [0] * (n + 1)
    temps2 = [0] * (n + 1)
    for _ in range(1, n + 1):
        maps = list(input().split())
        if maps[1] == "+" or maps[1] == "-" or maps[1] == "*" or maps[1] == "/":
            values[int(maps[0])] = maps[1]
            temps1[int(maps[0])] = int(maps[2])
            temps2[int(maps[0])] = int(maps[3])
        else:
            temps1[int(maps[0])] = int(maps[0])*2
            temps2[int(maps[0])] = int(maps[0])*2+1
            values[int(maps[0])] = int(maps[1])

    print("#{} {}".format(tc, int(postorder(1))))