n, m = map(int, input().split())
grid = []
for _ in range(n):
    line = list(map(int, input().split()))
    grid.append(line)

def find_sequence():
    sequence = []
    sequence.extend(grid)
    for i in range(n):
        col = []
        for row in grid:
            col.append(row[i])
        sequence.append(col)
    #print(sequence)
    answer = 0
    for line in sequence:
        #print('line')
        #print(line)
        for idx, val in enumerate(line):
            #print(idx, val)
            if idx + m - 1 >= n:
                #print('continue')
                continue
            #print(str(val) * m)
            #print(''.join(str(ele) for ele in line[idx:idx+m]))
            #print(str(val) * m in ''.join(str(ele) for ele in line[idx:idx+m]))
            if str(val) * m == ''.join(str(ele) for ele in line[idx:idx+m]):
                answer += 1
                #print(f"added, answer:{answer}")
                break 
    return answer

print(find_sequence())