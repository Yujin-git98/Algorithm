# 토마토 (BFS활용)
# 토마토는 격자 모양 상자의 칸에 하나씩 넣어서 보관한다.
# 하나의 토마토에 인접한 곳은 왼, 오, 앞, 뒤 네방향을 의미한다.
# 하루가 지나면 익은 토마토의 인접한 곳에 있는 익지않은 토마토들은 익게된다.
# 토마토 혼자 저절로 익는 경우가 없다고 가정할 떄 며칠이 지나면 다 익는지 최소 일수를 구해라

# 입력
# 1. 상자의 크기를 나타내는 두 정수 M가로, N세로
# 2. 토마토의 정보. 정수 1은 익은 토마토 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

#출력
# 토마토가 모두 익을 때까지 최소 날짜 출력
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지 못하는 상황이면 -1을 출력
from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

m, n =map(int, input().split()) #가로(행), 세로(열)
board=[list(map(int, input().split())) for _ in range(m)]
dq=deque()
dis=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if board[i][j]==1:
            dq.append((i, j))
while dq:
    tmp=dq.popleft()
    for i in range(4):
        xx=tmp[0]+dx[i]
        yy=tmp[1]+dy[i]
        if 0<=xx<m and 0<=yy<n and board[xx][yy]==0:
            board[xx][yy]=1
            dis[xx][yy]=dis[tmp[0]][tmp[1]]+1 # 부모보다 1더해서 넣는다. 최소 일수를 계산하기 위해
            dq.append((xx, yy))

flag=1
for i in range(m):
    for j in range(n):
        if board[i][j]==0: # 전체를 다 훑었는데도 안익은 토마토가 발생하면 -1 출력
            flag=0
result=0
if flag==1: # 다익는데 걸리는 일 중에서 최대값을 구함 그게 최솟값임
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                result=dis[i][j]
    print(result)
else:
    print(-1) # flag가 0이면 안익은 토마토가 발생했으므로 -1 출력
