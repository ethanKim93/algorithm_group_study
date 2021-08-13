#정수를 문자열로 변환
find_num=''
def atoi(num):

    str_num=['0','1','2','3','4','5','6','7','8',',9']

    find_num=str_num[num]

    return find_num


result=atoi(1)

print(result,type(result))