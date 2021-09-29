hexarr = "01D06079861D79F99F"
HEXDIC = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
          "D": 13, "E": 14, "F": 15}
cac = 0
total = []
for i in range(len(hexarr) - 1, -1, -1):
    tmp = hexarr[i]
    cac = HEXDIC.get(tmp)
    p = []
    for i in range(0, 4):
        p.append(cac & (1 << i))

    for i in range(len(p)):
        if p[i]:
            total.insert(0, 1)
        else:
            total.insert(0, 0)

total = ''.join(map(str, total))
print(total)
