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

xlist = XtoB(alist) # binlist

amho_list = ['001101','010011','111011','110001','100011','110111','001011','111101','011001','101111']

ans = []
cnt = 0
for i in range(len(xlist)):
    if cnt: # Move backward
        cnt -= 1
        continue

    if xlist[i:i+6] in amho_list: # find amho
        ans.append(amho_list.index(xlist[i:i+6]))
        cnt = 5



print(*ans)

# 0DEC