#1

a = input()
b = list(a)

for i in range(len(a)//2):
    b[i], b[len(a)-1-i] = b[len(a)-1-i], b[i]

print(b)


#2
a = input()
print(a[::-1])


#3
a=input()
bin_list=[]
for i in range(len(a)):
    bin_list.append(a[len(a)-1-i])

print(''.join(bin_list))