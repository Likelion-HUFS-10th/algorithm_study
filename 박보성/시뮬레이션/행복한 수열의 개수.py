n,m=map(int, input().split())
matrix=list(list(map(int, input().split())) for _ in range(n))

if n==1:
    if m==1:
        print(2)
    if m>1:
        print(0)
elif n>1:
    happy_sequence=0
    for i in range(n):
        row_cnt=1
        for j in range(n-1):
            if matrix[i][j]==matrix[i][j+1]:
                row_cnt+=1
            else:
                row_cnt=1
            if row_cnt>=m:
                happy_sequence+=1
                break

    for i in range(n):   
        col_cnt=1      
        for j in range(n-1):
            if matrix[j][i]==matrix[j+1][i]:
                col_cnt+=1
            else:
                col_cnt=1
            if col_cnt>=m:
                happy_sequence+=1
                break
    print(happy_sequence)
