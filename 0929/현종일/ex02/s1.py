n_16 = "01D06079861D79F99F"
n_2 = ""
for idx in range(len(n_16)):
    n_10 = int(n_16[idx], 16)
    tmp = format(n_10, 'b')
    if len(tmp) < 4:
        while len(tmp) != 4:
            tmp = '0'+tmp
    n_2 += tmp

for i in range(len(n_2)//7+1):
    temp = n_2[i*7:(i+1)*7]
    if len(temp) < 7:
        while len(temp) != 7:
            temp = '0' + temp
    result = 0
    for k, j in enumerate(temp):
        if j == "1":
            result += 2**(6-k)
    print(result, end=" ") if i == len(n_2)//7 else print(result, end=", ")




