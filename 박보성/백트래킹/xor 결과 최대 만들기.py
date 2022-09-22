from functools import reduce
from itertools import combinations

n,m=map(int,input().split())
array=list(map(int,input().split()))

maximum=-1
for c in combinations(array,m):
    maximum=max(maximum, reduce(lambda x,y: x^y, c))
print(maximum)
