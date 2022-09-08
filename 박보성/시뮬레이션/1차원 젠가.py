n=int(input())
array=list(int(input()) for _ in range(n))

s1,e1=map(int, input().split())
s2,e2=map(int, input().split())

array=array[:s1-1]+array[e1:]
array=array[:s2-1]+array[e2:]
print(len(array))
for a in array:
    print(a)
