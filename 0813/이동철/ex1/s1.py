s = input()
# reverse_s = s[::-1]
# print(reverse_s)

# s_reverse = ''
# for char in s:
#     s_reverse = char + s_reverse
# print(s_reverse)

s_list = list(s)
for i in range(len(s)//2):
    s_list[i], s_list[len(s_list)-1-i] = s_list[len(s_list)-1-i], s_list[i]
print(*s_list, sep='')


