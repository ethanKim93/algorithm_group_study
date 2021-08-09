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

    if n<10 & counts[n]>=1 | n+1<10 & counts[n+1]>=1 | n+2<10 & counts[n+2]>=1:
        counts[n]-=1
        counts[n+1]-=1
        counts[n+2]-=1
        run+=1
        continue

    n+=1


if(run+tri==2):
    print('baby_gin')
