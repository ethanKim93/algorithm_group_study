s = 'Reverse this strings'

news = ''
for i in range(len(s)-1, -1, -1):
    news += s[i]

print(news)


# for i in range(len(s)//2):
#     s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]