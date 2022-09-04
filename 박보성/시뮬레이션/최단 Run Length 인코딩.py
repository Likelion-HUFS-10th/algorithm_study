a=input()

def encoder(a):
    string=a[0]
    cnt=1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            cnt+=1
        else:
            string+=str(cnt)+a[i+1]
            cnt=1
    string+=str(cnt)
    return len(string)

answer=float("inf")
for i in range(len(a)):
    string=a[i:]+a[:i]
    answer=min(answer,encoder(string))
print(answer)
