def itoa(kanji):
    total = 0
    for i in range(len(kanji)):
        total *= 10
        total += ord(kanji[i]) - 48
    return total


n = itoa(input())
print(n)    #음수일때는 앞에 -넣어서 그냥 출력 ㄱㄱ



# def atoi(n):
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     ans = ''
#     while True:
#         num = n % 10  # 1의 자리부터 확인
#         ans += numbers[num]
#         n //= 10
#         if n == 0:
#             break
#     return ans[::-1]
# 
# 
# number = int(input())
# a = atoi(number)
# print(a)


# def itoa(nums,s):
#     llist = []
#     while n > 0 :
#         num = nums % 10 # 맨 뒤에서부터
#         llist.insert(0, chr(num + 48)) # 추출하고 리스트에 담아주기
#         nums = int(nums//10)
#     s = "".join(llist)
#     print(s)

