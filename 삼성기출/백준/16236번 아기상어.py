# 16236번 아기 상어
# NxN 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다.
# 한칸에 물고기 최대 1마리 존재
# 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다.
# 가장 처음에 아기 상어의 크기는 2이고 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
# 따라서 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 잇는 칸은 지나 갈 수 있다.
# 아기 상어가 어디로 이동할지 결정하는 방법
# 1. 더이상 먹을 수 있는 물고기가 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다 : *거리->행->열 순으로 정렬
#   - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야 하는 칸의 개수의 최솟값이다.
#   - 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다.
# 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹고 그 칸은 빈칸이 된다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.
# 예를 들어 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
# 공간의 상태가 주어졌을 때 아기 상어가 몇 초동안 엄마상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구해라
from collections import deque


n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]

dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]

cnt=0
size=2

#상어 위치
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            x=i
            y=j

def dfs(x, y, size):
    visited=[[-1]*n for _ in range(n)] # 방문 여부 체크
    distance=[[0]*n for _ in range(n)] # 거리
    q=deque()
    q.append((x,y)) # 초기 위치(상어 위치)로 초기화
    visited[x][y]=1 # 초기 위치 방문 체크
    temp=[]
    while q:
        cur_x, cur_y=q.popleft()
        for i in range(4):
            nx=cur_x+dx[i]
            ny=cur_y+dy[i]
            if not (0<=nx<n and 0<=ny<n):
                continue
            if visited[nx][ny]!=-1:
                continue
            if graph[nx][ny]<=size: # 움직이는 것은 size가 작거나 같은 곳만 가능
                q.append((nx, ny))
                visited[nx][ny]=1
                distance[nx][ny]=distance[cur_x][cur_y]+1
                if graph[nx][ny]<size and graph[nx][ny]!=0: # 먹는 것은 size가 작은 것만 가능
                    temp.append((nx, ny, distance[nx][ny])) # 현재 상어와 근처 물고기 중 거리를 측정
    # 거리가 짧고, 행이 작고, 열이 작은 물고기를 맨 뒤로 정렬 (내림차준)
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1])) #sort로 하면 안됨

cnt=0
result=0
graph[x][y]=0 #현재 상어의 위치를 0으로 초기환
while True:
    shark=dfs(x, y, size)
    if len(shark)==0:
        break
    nx, ny, dist = shark.pop() # 거리가 짧고 행이 작고, 열이 작은 물고기 

    result+=dist # 이동거리만큼 시간이 걸림
    graph[nx][ny]=0 # 이동한 곳은 상어가 물고기를 잡아먹었으므로 0으로 초기화

    x, y=nx, ny # nx, ny로 업데이트
    cnt+=1
    if cnt==size: # 이동횟수가 크기와 같을 경우 크기를 1만큼 증가
        size+=1
        cnt=0
print(result)

