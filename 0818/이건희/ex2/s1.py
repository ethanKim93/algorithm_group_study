import sys
sys.stdin = open("input.txt")

for tc in range(2):
    maps = list(input())
    temps = []
    for i in maps:
        if i == "(":
            temps.append(i)
        elif i == ")":
            if temps:
                temps.pop()
            else:
                print(False)
                break

    if temps:
        print(False)
    else:
        print(True)
