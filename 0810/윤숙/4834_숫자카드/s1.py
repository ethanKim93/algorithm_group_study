

T=int(input())

count=[]*10
for tc in range(1,T+1):
    n=int(input())
    card_number=list(map(int, input()))

    for i in card_number:
        count[i]+=1



    print(count)
