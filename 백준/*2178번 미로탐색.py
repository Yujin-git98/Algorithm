# 2178번 미로 탐색
# nxm 크기의 배열로 표현되는 미로가 있다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때 (1,1)에서 출발하여 (n,m)의 위치로 이동할 때
# 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
from collections import deque
n, m = map(int, input().split()) # 행 열
board=[list(map(int,input())) for _ in range(n)]
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]

def bfs(i, j):
    #cnt=1 # 시작 위치도 포함
    dq=deque()
    dq.append([i, j])
    #board[i][j]=0 # 방문했으니까 0
    while dq:
        x, y=dq.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==1:
                    board[nx][ny]=board[x][y]+1
                    dq.append([nx, ny])
    return board[n-1][m-1]

print(bfs(0,0))
