def my_itoa(n):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    while n > 0:
        temp = n % 10
        for i in range(10):
            if i == temp:
                result = nums[i] + result
                break
        n -= temp
        n /= 10
    return result


print(my_itoa(123))
print(type(my_itoa(123)))