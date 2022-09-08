import math
from collections import deque

n,m,q=map(int, input().split())
matrix=list(list(map(int, input().split())) for _ in range(n))

dx=[0,1,0,-1,0]
dy=[0,0,1,0,-1]

def check(x,y):
    adjacent=list()
    for i in range(5):
        if 0<=x+dx[i]<m and 0<=y+dy[i]<n:
            adjacent.append(matrix[y+dy[i]][x+dx[i]])
    return math.floor(sum(adjacent)/len(adjacent))

for _ in range(q):
    r1,c1,r2,c2=map(int, input().split())

    rotation_array=list()
    for x in range(c1-1,c2):
        rotation_array.append(matrix[r1-1][x])
    for y in range(r1,r2):
        rotation_array.append(matrix[y][c2-1])
    for x in range(c2-2,c1-1,-1):
        rotation_array.append(matrix[r2-1][x])
    for y in range(r2-1,r1-1,-1):
        rotation_array.append(matrix[y][c1-1])

    rotation_array=[rotation_array.pop()]+rotation_array[:n*m-1]
    rotation_array=deque(rotation_array)
    for x in range(c1-1,c2):
        matrix[r1-1][x]=rotation_array.popleft()
    for y in range(r1,r2):
        matrix[y][c2-1]=rotation_array.popleft()
    for x in range(c2-2,c1-1,-1):
        matrix[r2-1][x]=rotation_array.popleft()
    for y in range(r2-1,r1-1,-1):
        matrix[y][c1-1]=rotation_array.popleft()
    
    medium_array=deque()
    for x in range(c1-1,c2):
        for y in range(r1-1,r2):
            medium_array.append(check(x,y))

    for x in range(c1-1,c2):
        for y in range(r1-1,r2):
            matrix[y][x]=medium_array.popleft()

for m in matrix:
    print(*m)
