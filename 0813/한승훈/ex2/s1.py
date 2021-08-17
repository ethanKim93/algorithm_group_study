number = int(input())

def itoa(n):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ans = ''
    while True:
        num = n % 10  # 1의 자리부터 확인
        ans += numbers[num]
        n //= 10
        if n == 0:
            break
    return ans[::-1]

a = itoa(number)
print(a)


