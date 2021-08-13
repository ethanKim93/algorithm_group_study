# atoi (문자 -> 숫자)
# python의 int()
# ascii to integer
def atoi(my_str):
    value = 0
    i = 0

    while i < len(my_str):
        # 문자에서 0번째 값부터 꺼내와서
        char = my_str[i]

        # 0과 9 사이에 있는 값? -> 한 자릿수 
        if ord('0') <= ord(char) <= ord('9'):
            # 자릿수를 만들어 준다.
            # 1은 49 --> 49 - 48 = 1
            # digit은 1
            digit = ord(char) - ord('0')
        # 그렇지 않으면 숫자가 아닌 값 -> 0 return
        else:
            break

        """
        1. 1이 digit으로 들어오는 시점에 value는 초깃값이 0이다. 그럼 (0 * 10) + 1 이기 때문에 value는 1이 된다.  
        2. 다음 digit은 2가 된다. 이제 기존 value가 1이기 때문에 (1 * 10) + 2 -> 12가 된다.
        3. 마지막은 digit이 3이 된다. value는 12인 상태 -> (12 * 10) + 3 -> 123이 된다. 
        
        즉, 자릿수가 첫 digit을 시작으로 하나씩 늘어나며 숫자가 뒤에 붙어가는 형태로 만들어진다.
        """
        value = (value * 10) + digit
        # 다음 자리를 확인하자
        i += 1
    return value

my_str = '123'
print(my_str, type(my_str))

my_int1 = atoi(my_str)
print(my_int1, type(my_int1))

my_int2 = int(my_str)
print(my_int2, type(my_int2))


print('--------------------------------------')


# itoa (숫자 -> 문자)
# int to ascii
# python의 str()
def itoa(my_int):
    my_str = []

    # 0인 경우
    if not my_int:
        return chr(ord('0'))
        # return chr(48)

    # 0이 아닌 경우
    while my_int != 0:
        #1. 넘어온 수를 나머지 저장 -> 3, 2, 1 이런식으로 저장
        r = my_int % 10

        #2. 문자열로 추가 -> 아스키코드 활용
        """
        여기서의 최종 목표는 숫자3을 문자3으로 만들어 주는 것
        1. 문자 3, 2, 1의 아스키코드 값은  51, 50, 49다. 
        2. 51, 50, 49를 만들어 이를 chr()에 넣어주면 우리가 원하는 '3', '2', '1'을 얻게 된다.
        3. 그럼 어떻게 만들어 주지? 0을 더해주면 된다! 어떻게? 
        4. ord('0')을 통해 문자 0의 값인 48을 얻을 수 있고 3, 2, 1 값에 더해 문자열 값을 얻자
        """
        my_str.append(chr(r + ord('0')))
        # print(type(chr(3 + ord('0')))) # '3'
        # print(chr(2 + ord('0'))) # '2'
        # print(chr(1 + ord('0'))) # '1'

        #3. 해당 정수의 몫을 할당 -> 123이면 12 / 12라면 1 이런식으로 진행
        my_int //= 10
    
    # 반복문 이후 뒤집기 -> ['3', '2', '1'] 형태로 들어오기 때문
    my_str.reverse()
    # 최종 붙여서 문자열로 만들어 반환
    my_str = ''.join(my_str)
    return my_str

my_num = 123
print(my_num, type(my_num))
my_num = 0
my_str1 = itoa(my_num)
print(my_str1, type(my_str1))

my_str2 = str(my_num)
print(my_str2, type(my_str2))