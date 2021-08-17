string = input()

sub = False
result = 0
for idx in range(len(string)-1, -1, -1):
    if string[idx] == '-':
        sub = True
    else:
        result += (10**(len(string)- idx - 1)) * (ord(string[idx]) - 48)
    idx += 1
result *= (-1) ** sub
print(result)