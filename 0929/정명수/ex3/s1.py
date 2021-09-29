password = {"001101": 0, "010011": 1, "111011": 2, "110001": 3, "100011": 4, "110111": 5, "001011": 6, "111101": 7, "011001": 8, "101111": 9}

data = input()
num = ''
answer=[]
k = 0
for i in data:
    num += bin(int(i, 16))[2:].zfill(4) # 16진수 > 10진수 > 2진수 > 4자리 형태
while k<len(num):
    try:
        password[num[k:k+6]]
        answer.append(password[num[k:k+6]])
        k += 6
    except:
        k += 1
print(answer)