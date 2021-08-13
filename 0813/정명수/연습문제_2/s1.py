def itoa(number):
    munja=''
    while number>=1:
        num = number%10
        number = number//10
        munja = chr(num+48) +munja
    return munja
a = int(input())
print(itoa(a))