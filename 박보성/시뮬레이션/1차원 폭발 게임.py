n,m=map(int, input().split())
bambs=list(int(input()) for _ in range(n))

check=n
while True:
    if m==1:
        bambs=[]
        break
    cnt=1
    start=0
    for i in range(len(bambs)-1):
        
        if bambs[i]==bambs[i+1]:
            cnt+=1
        else:
            if cnt>=m:
                for j in range(start,i+1):
                    bambs[j]=0
            start=i+1
            cnt=1
    if cnt>=m:
        for j in range(start,len(bambs)):
            bambs[j]=0  
    bambs=[b for b in bambs if b!=0]   
    if check==len(bambs):
        break
    check=len(bambs)
    
print(len(bambs))
for b in bambs:
    print(b)
