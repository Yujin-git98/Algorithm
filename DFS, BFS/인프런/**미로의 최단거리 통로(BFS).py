# 미로의 최단거리 통로
# 7*7 격자판 미로를 탈출하는 최단경로의 경로수 출력
# 경로수는 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다.
# 출발점은 격자의 (1, 1) 좌표이고 탈출 도착점은 (7, 7) 좌표이다.
# 격자판의 1은 벽이고 0은 도로이다.
# 격자판의 움직임은 상하좌우로만 움직인다.

#입력
# 7*7 격자판의 정보가 주어진다.

#출력
# 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1을 출력한다.
from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
board=[list(map(int, input().split())) for _ in range(7)] # 2차원 배열로 7*7 격자판 미로 생성
dis=[[0]*7 for _ in range(7)]
dq=deque()
board[0][0]=1
while dq:
    tmp=dq.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0: # 격자 안에 해당하고 벽이 아닌경우
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            dq.append((x, y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])
