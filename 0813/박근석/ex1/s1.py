# temp를 활용하여 리버스
word = 'algorithm'
word = list(word)
for i in range(len(word)//2):
    temp = word[i]
    word[i] = word[-1-i]
    word[-1-i] = temp

print(''.join(word))

# slice를 활용하여 리버스
word = 'algorithm'
print(word[::-1])

