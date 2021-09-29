def XtoB(temps):
    wan = ""
    for i in temps:
        base = ""
        if i in [str(j) for j in range(10)]:
            for w in range(4):
                if int(i) & (1<<w):
                    base = "1" + base
                else:
                    base = "0" + base

        else:
            for w in range(4):
                if xdic[i] & (1<<w):
                    base = "1" + base
                else:
                    base = "0" + base

        wan += base
    return wan

alist = list(input()) # hexa list
xdic = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

blist = XtoB(alist) # bin list

# print(bin -> int)
cnt = 0
temps = ""
for i in range(len(blist)):
    temps += blist[i]
    cnt += 1

    if cnt == 7:
        print(int(temps,2), end=", ")
        cnt = 0
        temps = ""

print(int(temps,2))

# 01D06079861D79F99F
# 000011111001011110100011
# 0F97A3