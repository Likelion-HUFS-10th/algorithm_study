n, m, q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]
winds = []

for _ in range(q):
    r, d = input().split()
    winds.append([int(r), d])

def shift(r, d):
    # print(f'r: {r}, d: {d}')
    # print(f'before: {building[r]}')
    if d == 'L':
        building[r] = building[r][-1:] + building[r][:-1]
    else:
        building[r] = building[r][1:] + building[r][:1]
    # print(f'after: {building[r]}')

def swift_direction(d):
    d = 'R' if d == 'L' else 'L'
    return d

def has_same_num(row1, row2):
    for i in range(m):
        if row1[i] == row2[i]:
            return True
        else: continue
    return False

for wind in winds:
    r, d = wind[0]-1, wind[1]
    shift(r, d)
    d_d, u_d = d, d
    for row in range(r, n):
        if row >= n-1: break
        d_d = swift_direction(d_d)
        if has_same_num(building[row], building[row+1]):
            shift(row+1, d_d)
        else: break
            
    for row in range(r, -1, -1):
        if row-1 < 0: break
        u_d = swift_direction(u_d)
        if has_same_num(building[row], building[row-1]):
            shift(row-1, u_d)
        else: break
        
for floor in building:
    print(*floor)
    