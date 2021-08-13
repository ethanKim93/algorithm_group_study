
#0은 48
#문자열을 정수로 변환
def atoi(str_num):
    N_t=int(str_num)
    arr_num=[]
    while True:
        N_d=N_t%10
        for i in range(48,58):
            if N_d==str(i):
                arr_num.append(str(i))


        N_t = N_t/10


    int_num="".join(arr_num)

    return int(int_num)




# 정수를 문자열로 변환
# def itoa(num):



result=atoi('1245')

print(result,type(result))