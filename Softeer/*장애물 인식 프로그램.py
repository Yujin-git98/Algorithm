# 장애물 인식 프로그램
# 장애물과 도로 인식할 수 있는 프로그램을 만들라는 업무가 주어짐/
# 정사각형 모양의 지도에 장애물이 있는 곳은 1, 도로가 있는 곳은 0을 나타낸다.
# 이 지도를 가지고 연결된 장애물들의 모임인 블록을 정의하고, 블록에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 장애물이 좌우, 혹은 아래위로 붙어있는 경우를 말한다.
# 대각선 상에 장애물이 있는 경우는 연결된 것이 아니다.
# 지도를 입력하여 장애물 블록수를 출력하고 각 블록에 속하는 장애물의 수를 오름차순으로 정렬하여 출력해라
from collections import deque
n=int(input())
#board=[list(map(int, input().split())) for _ in range(n)]
board=[]
for i in range(n):
    board.append(list(map(int, input())))
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]
cnt=0
def bfs(i, j):
    global cnt
    cnt = 1
    visited[i][j]=1
    dq=deque()
    dq.append([i,j])
    while dq:
        x, y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                a=board[nx][ny]
                if visited[nx][ny]==0 and board[nx][ny]==1:
                    cnt+=1
                    visited[nx][ny]=1
                    dq.append([nx, ny])
    result.append(cnt)

result=[] # 장애물 개수
visited=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and board[i][j]==1:
            bfs(i, j)

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])

