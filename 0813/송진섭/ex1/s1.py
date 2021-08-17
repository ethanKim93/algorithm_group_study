s = 'Reverse this strings'
print(s[::-1])

s_list =list(s)
n = len(s_list)
print(s_list)
for i in range(n//2):
    s_list[i], s_list[(n-1-i)] = s_list[(n-1-i)], s_list[i]
print((s_list))