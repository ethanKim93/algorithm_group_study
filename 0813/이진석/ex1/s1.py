string_1 = 'algorithm'          # slice notation
reverse_string_1 = string_1[::-1]
print(string_1)
print(reverse_string_1)

string_2 = 'SSAFY'              # list를 이용한 뒤집기
str_list = list(string_2)
for i in range(len(str_list)//2):
    str_list[i], str_list[-(i+1)] = str_list[-(i+1)], str_list[i]

reverse_string_2 = ''.join(str_list)
print(string_2)
print(reverse_string_2)

string_3 = 'Python'             # 자기 문자열을 이용한 뒤집기
print(string_3)
temp_str = ''
for i in range(len(string_3)):
    temp_str += string_3[-(i+1)]
string_3 = temp_str
print(string_3)

string_4 = 'SAMSUNG'            # reversed() 내장함수 사용
print(string_4)
print(''.join(reversed(string_4)))