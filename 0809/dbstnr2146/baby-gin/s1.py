card=list(map(int,input().split()))

counts=[0]*10

for i in card:
    counts[i]+=1

tri=0
run=0
n=0

while n<10:
    if counts[n]>=3:
        counts[n]-=3
        tri+=1
        continue

    if counts[n]>=1:
        for i in range(0,3):
            if n+i<10:
                counts[n+i]-=1
                run+=1
        continue

    n+=1

if run%3==0:
    run=run//3

print(run)

if(run+tri==2):
    print('baby_gin')
