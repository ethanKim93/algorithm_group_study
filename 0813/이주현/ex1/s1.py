string = input()
result = ''

for idx in range(len(string)-1,-1,-1):
    result += string[idx]

print(result)