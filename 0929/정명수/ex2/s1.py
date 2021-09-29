data = input()
num = ''
for i in data:
    num += bin(int(i, 16))[2:].zfill(4) # 16진수 > 10진수 > 2진수 > 4자리 형태
for j in range(0,len(num),7):
    ans = int(num[j:j+7],2)
    print(ans)