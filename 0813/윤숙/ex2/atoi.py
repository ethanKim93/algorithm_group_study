
#0은 48
#문자열을 정수로 변환
def atoi(str_num):
    N_t=int(str_num)
    arr_num=[]
    while True:
        if N_t==0:
            arr_num.reverse()
            return arr_num

        N_d=N_t%10
        for i in range(48,58):
            if N_d==int(chr(i)):
                arr_num.append(N_d)

        N_t = N_t//10


# 정수를 문자열로 변환
def itoa(num):
    N_t = num
    arr_num = []
    while True:
        if N_t == 0:
            arr_num.reverse()
            return arr_num

        N_d=N_t%10
        for i in range(48,58):
            if N_d==int(chr(i)):
                arr_num.append(str(chr(i)))

        N_t = N_t//10







result1=atoi('1245')
result2=itoa(1245)

print(result1)
print(result2)