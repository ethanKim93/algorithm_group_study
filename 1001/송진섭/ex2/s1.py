nums = list(map(int, input()))

num_list = [0] * 10
for num in nums:
    num_list[num] += 1

tri = run = 0
i = 0
while i < 10:
    if num_list[i] >= 3:
        num_list[i] -= 3
        tri += 1
        continue
    if num_list[i] >= 1 and num_list[i+1] >= 1 and num_list[i+2] >= 1:
        num_list[i] -= 1
        num_list[i+1] -= 1
        num_list[i+2] -= 1
        run += 1
        continue
    i += 1

ans = 'Baby Gin' if run + tri == 2 else 'X'
print(ans)
