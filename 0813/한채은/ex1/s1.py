

# 1 [slice]

S = 'algorithm'

reversed_S = S[::-1]
print(reversed_S)

# 2[reversed]

S = 'algorithm'

reversed_S =''.join(reversed(S))
print(reversed_S)

# 3[temp]

S = list('algorithm')

left = 0
right = (len(S) - 1)

while left < right:
    temp = S[left]
    S[left] = S[right]
    S[right] = temp
    left += 1
    right -= 1

print(''.join(S))


