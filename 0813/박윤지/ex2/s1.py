def itoa(num, string):
    my_str = []
    while num >= 1 :
        one = num % 10
        num //= 10
        my_str = [chr(one + 48)] + my_str
        print(my_str)
    string = "".join(my_str)
    return string

string = ''
print(type(itoa(123, string)))