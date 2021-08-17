def itoa(number):
    munja=''
    if number > 0:
        while number>=1:
            num = number%10
            number = number//10
            munja = chr(num+48) +munja
        return munja
    elif number < 0:
        number *= -1
        while number>=1:
            num = number%10
            number = number//10
            munja = chr(num+48) +munja
        return '-'+munja
    else:
        return chr(number+48)

def atoi(munja):
    number = 0
    j=len(munja)-1
    for i in munja:
        number += (ord(i)-48)*10**j
        j -= 1
    return number
a,b = int(input()),input()
print(itoa(a))
print(type(itoa(a)))
print(atoi(b))
print(type(atoi(b)))