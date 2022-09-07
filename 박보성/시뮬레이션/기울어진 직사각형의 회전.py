n=int(input())
matrix=list(list(map(int, input().split())) for _ in range(n))
r, c, m1, m2, m3, m4, d=map(int, input().split())

dx=[1,-1,-1,1]
dy=[-1,-1,1,1]

rotate_list=list()
for i, n in enumerate([m1, m2, m3, m4]):
    for _ in range(n):
        r+=dy[i]
        c+=dx[i]
        rotate_list.append(matrix[r-1][c-1])
if d:
    for i, n in enumerate([m1, m2, m3, m4]):
        for _ in range(n):
            matrix[r-1][c-1]=rotate_list.pop(0)
            r+=dy[i]
            c+=dx[i]
    for m in matrix:
        print(*m)
else:
    rotate_list=rotate_list[-1:]+rotate_list[:-1]
    for i, n in enumerate([m1, m2, m3, m4]):
        for _ in range(n):
            r+=dy[i]
            c+=dx[i]
            matrix[r-1][c-1]=rotate_list.pop(0)
    for m in matrix:
        print(*m)
