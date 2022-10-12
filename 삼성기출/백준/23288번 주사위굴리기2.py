# 23288번 주사위 굴리기2
# 크기가 NxM인 지도, 좌표는 행, 열 = r,c
# 지도의 오른쪽은 동쪽, 위쪽은 북쪽
# 가장 왼쪽 위 좌표가 (1,1), 가장 오른쪽 아래 좌표가 (N,M)
# 주사위는 지도 위에 윗면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있다.
# 놓여진 곳의 좌표는 (1, 1)이다.
# 지도의 각 칸에도 정수가 하나씩 있다. 가장 처음에 주사위의 이동방향은 동쪽이다.
# 주사위의 이동 한번은 다음과 같은 방식으로 이루어진다.
# 1. 주사위가 이동 방향으로 한 칸 굴러간다.
# 만약, 이동방향에 칸이 없다면 이동방향을 반대로 한 다음 한칸굴러간다.
# 2. 주사위가 도착한 칸(x, y)에 대한 점수를 획득한다.
# 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸(x,y)에 있는 정수 B를 비교해 이동 방향을 결정
# A>B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
# A<B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
# A=B인 경우 이동 방향에 변화는 없다.
# 칸(x,y)에 대한 점수는 다음과 같이 구할 수 있다.
# (x, y)에 있는 정수를 B라고 했을 때, (x, y)에서
# 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다.
# 이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다. 여기서 점수는 B와 C를 곱한 값이다.
# 보드의 크기와 각 칸에 있는 정수, 주사위의 이동 횟수 K가 주어졌을 때 각 이동에서 획득하는 점수의 합을 구해보

from collections import deque
import copy

n, m, k = map(int, input().split())
data=[list(map(int, input().split())) for _ in range(n)]
ball = [2, 4, 1, 3, 5, 6] # 초기 주사위 (전면, 왼쪽, 상단, 오른쪽, 후면, 바닥)
dir=0 #초기방향(동쪽)

# 동 남 서 북(시계방향)
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
x,y=0,0 # 주사위 초기 위치
result=0 #최종점수

def ball_move(x, y, dir):
    nx=x+dx[dir]
    ny=y+dy[dir]

    if not (0<=nx<n and 0<=ny<m): # 이동방향에 칸이 없는 경우
        nd=(dir+2)%4 # 반대방향
        nx=x+dx[nd]
        ny=y+dy[nd]
        return [nx, ny, nd]
    # 이동방향에 칸이 있는 경우
    return [nx, ny, dir]

def change_ball(ball, dir):
    # (전면, 왼쪽, 상단, 오른쪽, 후면 바닥)
    # 동쪽이동 : 왼쪽, 상단, 오른쪽, 바닥
    if dir == 0:
        ball[1], ball[2], ball[3], ball[5] = ball[5], ball[1], ball[2], ball[3]
        # 남쪽 이동 (전면, 상단, 후면, 바닥)
    elif dir == 1:
        ball[0], ball[2], ball[4], ball[5] = ball[5], ball[0], ball[2], ball[4]
        # 서쪽 이동 (왼쪽, 상단, 오른쪽, 바닥)
    elif dir == 2:
        ball[1], ball[2], ball[3], ball[5] = ball[2], ball[3], ball[5], ball[1]
        # 북쪽 이동 (전면, 상단, 후면, 바닥)
    elif dir == 3:
        ball[0], ball[2], ball[4], ball[5] = ball[2], ball[4], ball[5], ball[0]

    return ball

#연속해서 이동할 수 있는 칸의 개수 조사
def bfs(x, y):
    cnt=1 # 맨처음 칸 포함
    visited=[[0]*m for _ in range(n)]
    #visited[x][y] = 1
    q=deque()
    q.append((x, y))
    while q:
        r, c = q.popleft()
        visited[r][c]=1
        for i in range(4):
            nr=r+dx[i]
            nc=c+dy[i]
            if not(0<=nr<n and 0<=nc<m):
                continue
            if data[r][c]==data[nr][nc] and not visited[nr][nc]:
                visited[nr][nc]=1
                q.append((nr, nc))
                cnt+=1
    return cnt

for _ in range(k):
    # 주사위 이동
    x, y, dir=ball_move(x, y, dir)
    ball = change_ball(ball, dir)
    # 주사위가 도착한 칸에 대한 점수 계싼
    count=bfs(x, y)
    result+=data[x][y]*count

    # 주사위 이동방향 결정
    a, b = ball[5], data[x][y]
    # a>B인 경우 이동방향을 90도 시계 방향으로 회전
    if a>b:
        dir=(dir+1)%4
    # a<b인 경우 이동 방향을 90도 반시계 방향으로 회전
    elif a<b:
        dir=(dir-1)
        if dir==-1:
            dir=3
print(result)




