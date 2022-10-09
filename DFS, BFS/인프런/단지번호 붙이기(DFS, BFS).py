# 단지번호 붙이기(DFS, BFS)
# 정사각형 모댱의 지도. 1은 집이 있는 곳, 0은 집이 없는곳
# 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우 혹은 아래위로 다른 집이 잇는 경우. 대각선상에 집이 있는 경우는 연결된것이 아님
# 지도를 입력하여 단지수를 출력하고 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

# 입력
# 지도의 크기 n, 지도의 정보

# 출력
# 총 단지수, 각 단지내의 집의 수를 오름차순으로 정렬하여 한줄에 하나씩 출력
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]


#DFS
def dfs(x, y):
    global cnt
    cnt+=1 #하나의 집좌표가 넘어옴
    map[x][y]=0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and map[xx][yy]==1:
            dfs(xx, yy)



n=int(input())
map=[list(map(int, input())) for _ in range(n)]
res=[] # 한단지의 집의 개수
for i in range(n):
    for j in range(n):
        if map[i][j]==1:
            cnt=0 # 현재 단지의 집의 개수
            dfs(i, j)
            res.append(cnt)

res.sort()
print(len(res))
for i in res:
    print(i)

#BFS
from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
board=[list(map(int, input())) for _ in range(n)] # input().split()이 아니라 그냥 input()
cnt=0
res=[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            cnt=1
            while Q:
                tmp=Q.popleft()
                for k in range(4):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y]==0:
                        continue
                    board[x][y]=0
                    Q.append((x, y))
                    cnt+=1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)
