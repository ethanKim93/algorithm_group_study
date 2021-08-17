def fake_itoa(number, save):
    if number == 0: #0일 때
        save = chr(48) #0
    sign = ''
    if number < 0: #음수일 때
        sign = '-'
        number = -number
    while number: #number가 0이 아님
        save = chr(48+number%10) + save # 나머지를 왼쪽에 붙임
        number = number//10 # number를 10으로 나눈 몫
    save = sign + save #부호 처리
    print(save)

def fake_atoi(strings):
    sign = 1 # 부호
    num = 0 # 출력될 숫자
    if strings[0] == '-': # 부호의 시작이 음수
        strings = strings[1:] # 부호 빼준다
        sign = -1 # 부호 음수
    for string in strings: # 왼쪽부터 하나씩
        num = num*10 + ord(string)-48 # ASCII 코드 십진법
    print(num * sign) # 부호까지 고려

hey = ''
fake_itoa(-1234, hey)

fake_atoi('0')