pattern={
    '001101':0,
    '010011':1,
    '111011':2,
    '110001':3,
    '100011':4,
    '110111':5,
    '001011':6,
    '111101':7,
    '011001':8,
    '101111':9,
}
HEXDIC = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
          "D": 13, "E": 14, "F": 15}

hexarr="0269FAC9A0"
cac=0
total=[]
for i in range(len(hexarr)-1,-1,-1):
    tmp=hexarr[i]
    cac=HEXDIC.get(tmp)
    p=[]
    for i in range(0, 4):
        p.append(cac & (1<<i))

    for i in range(len(p)):
        if p[i]:
            total.insert(0,1)
        else:
            total.insert(0,0)
k=6
total=''.join(map(str,total))
print(total)
for i in range(len(total)-1,-1,-6):
    if total[i:i+k] in pattern:
        print(pattern.values())




