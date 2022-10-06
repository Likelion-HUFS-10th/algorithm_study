import sys
import copy

sys.setrecursionlimit(2500)

N, M = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
flooded = [[0 for _ in range(M)] for _ in range(N)]
max_comfy_zone = 0
answer = []

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

def calc_comfort_zone(x, y, phase, visited):
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and not flooded[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = phase
            calc_comfort_zone(nx, ny, phase, visited)

def dfs(phase, max_comfy_zone):
    # 반복: phase가 1씩 증가하며 flooded 업데이트 
    for i in range(N):
        for j in range(M):
            if grid[i][j] == phase:
                flooded[i][j] = phase

    # 안전지대 카운트를 위한 침수지역 깊은 복사본
    visited = copy.deepcopy(flooded)
    # 안전지대 카운트
    phase_comfy_zone = 0
    
    for i in range(N):
        for j in range(M):
            if not flooded[i][j] and not visited[i][j]:
                calc_comfort_zone(i, j, phase, visited)
                phase_comfy_zone += 1
    # print(f'phase_comfy_zone:{phase_comfy_zone}')
    max_comfy_zone = max(max_comfy_zone, phase_comfy_zone)

    # 종료 조건: 모든 집이 침수될 때
    if phase_comfy_zone == 0:
        answer.append(max_comfy_zone)
        if phase == 1:
            answer.append(phase)
        return


    dfs(phase+1, max_comfy_zone)
    # print('after')
    # print(f'phase:{phase}')
    # print(f'max_comfy_zone:{max_comfy_zone}')
    # print(f'phase_comfy_zone:{phase_comfy_zone}')
    if phase_comfy_zone == answer[0]:
        answer.append(phase)
    

dfs(1, max_comfy_zone)

max_comfy_zone = answer.pop(0)
K = sorted(answer)[0]
print(K, max_comfy_zone)