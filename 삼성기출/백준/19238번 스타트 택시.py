# 스타트 택시
# 손님을 도착지로 데려다줄때마다 연료가 충전되고 연료가 바닥나면 그 날의 업무가 종료
# M명의 승객을 태우는 것이 목표
# 활동영역은 NxN 크기의 격자, 각 칸은 비어 있거나 벽이 놓여있다.
# 택시가 빈칸에 있을 때 상하좌우로 인접한 빈칸으로 간다.
# 특정 위치로 이동할 때 항상 최단 경로로만 이동한다 -> BFS
# M명의 승객은 빈칸 중 하나에 서있으며, 다른 빈칸 중 하나로 이동하려고 한다.
# 여러 승객이 같이 탑승하는 경우는 없다. 따라서 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야한다.
# 태울 승객을 고를때 현재 위치에서 최단거리가 가장 짧은 승객을 고른다.
# 그런 승객이 여러 명이면 그 중 행 번호가 가장 작은 승객 -> 열번호가 가장 작은 승객을 고른다.
# 택시와 승객이 같은 위치에 서있으면 그 승객까지의 최단거리는 0이다.
# 연료는 한칸이동할 때마다 1만큼 소모된다. 한 승객을 이동시키면 소모한 연료양의 2배가 충전된다.
# 이동하는 도중 연료가 바닥나면 이동에 실패하고 그 날 업무가 끝난다.
# 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
from collections import deque

n, m, cost = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
car_x, car_y = map(int, input().split())
passenger = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(car_x, car_y): # 문제와 좌표와의 car_x값이 다름 1 차이남
    visited=[[-1]*n for _ in range(n)]
    q=deque()
    q.append((car_x, car_y))
    visited[car_x][car_y]=0 #0부터 시작 (주의)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if not (0<=nx<n and 0<=ny<n):
                continue
            if data[nx][ny]==1 or visited[nx][ny]!=-1:
                continue
            visited[nx][ny]=visited[x][y]+1
            q.append((nx, ny))
    return visited

def check_distance(visited, passenger):
    i=0
    for start_x, start_y, dest_x, dest_y in passenger:
        passenger[i].append(visited[start_x-1][start_y-1])
        i+=1
    passenger.sort(key=lambda x:(x[4], x[0], x[1]), reverse=True)

def solution(car_x, car_y):
    global cost
    while passenger:
        visited=bfs(car_x-1, car_y-1)
        check_distance(visited, passenger) # passenger에 최단거리 추가
        start_x, start_y, dest_x, dest_y, distance = passenger.pop()

        for temp in passenger:
            temp.pop()
        visited=bfs(start_x-1, start_y-1)
        distance2=visited[dest_x-1][dest_y-1]
        car_x, car_y=dest_x, dest_y

        if distance==-1 or distance2==-1:
            print(-1)
            return
        cost-=distance
        if cost<0:
            break
        cost-=distance2
        if cost<0:
            break
        cost+=distance2*2

    if cost<0:
        print(-1)
    else:
        print(cost)
solution(car_x, car_y)



