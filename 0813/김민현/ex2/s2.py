def atoi(int_x,str_y):
    int_list=[]
    
    flag = False
    if int_x < 0: #음수가 들어왔을때
        int_x *= -1
        flag = True

    if int_x == 0: #0이 들어왔을때
        str_num = ord('0')
        int_list.append(chr(str_num))
    else:
        while int_x > 0:
            str_num = int_x%10+ord('0')
            int_list.append(chr(str_num))
            int_x = int_x//10

    for i in int_list[::-1]:
        str_y += i
    
    if flag == True:
        str_y = '-'+str_y
    return str_y


def itoa(str_x,int_y):
   str_list = []
   flag = False
   for ch in str_x:
       if ch == '-':
           flag = True
           continue
       int_num = ord(ch) - ord('0')
       str_list.append(int_num)
   int_y = 0
   for i in range(len(str_list)):
       int_y += str_list[i]*(10**(len(str_list)-1-i))

   if flag == True:
       int_y *= -1
   return int_y

a =''
print(atoi(-123,a))
b = 0
print(itoa('-33',b))