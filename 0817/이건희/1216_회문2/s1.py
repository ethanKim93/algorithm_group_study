import sys
sys.stdin = open("input.txt")

for _ in range(1,11):
    tc = int(input())
    maps = [list(input()) for _ in range(100)]
    mx = 1
    # 가로
    for i in range(100):
        for x in range(100):
            for y in range(100-x+1):
                if maps[i][x:x+y] == maps[i][x:x+y][::-1]:
                    if mx < y:
                        mx = y

                # 세로
                col_word = ""
                for z in range(y):
                    col_word += maps[x + z][i]

                if col_word == col_word[::-1]:
                    if mx < y:
                        mx = y

    print("#{} {}".format(tc, mx))
