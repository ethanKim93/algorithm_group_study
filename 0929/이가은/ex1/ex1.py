question = input()

for i in range(0,len(question),7):
    result = 0
    for j in range(i, i+7):
        result += int(question[j])*(2**(6-(j%7)))
    print(result)