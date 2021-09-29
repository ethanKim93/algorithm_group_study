n_16 = "0269FAC9A0"
n_2 = ""

pattern = ["001101", "010011", "111011", "110001", "100011", "110111", "001011", " 111101", "011001", "101111"]
for idx in range(len(n_16)):
    n_10 = int(n_16[idx], 16)
    tmp = format(n_10, 'b')
    if len(tmp) < 4:
        while len(tmp) != 4:
            tmp = '0'+tmp
    n_2 += tmp

n_2 = n_2[::-1]

i = 0
result = []
while i < len(n_2):
    if n_2[i] == '1':
        temp = n_2[i:i+6]
        temp = temp[::-1]
        for k in range(10):
            if temp == pattern[k]:
                result.append(k)
        i += 6
    else:
        i += 1

while result:
    r1 = result.pop()
    print(r1, end=", ") if len(result) > 0 else print(r1)

