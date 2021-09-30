data = input()
for i in range(0,len(data),7):
    a=data[i:i+7]
    a = int(a, 2)
    print(a)