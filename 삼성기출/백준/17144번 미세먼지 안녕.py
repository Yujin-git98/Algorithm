# 17144번 미세먼지 안녕!
# 집의 크기 RxC 격자판, R행 C열
# 공기청정기는 항상 1번열에 설치, 크기는 두 행을 차지
# 공기청정기 설치되지 않은 칸에 미세먼지가 있고, (r,c)에 있는 미세먼지양은 Ar,c이다.
# 1초동안 아래 적힌 일이 순서대로 일어난다.
# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
#  (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기 청정기가 있거나 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# r,c에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
# 2. 공기청정기가 작동한다.
#  공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계 방향으로 순환하고 아래쪽 공기청정기의 바람은 시계 방향으로 순환한다
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고 공기청정기로 들어간 미세먼지는 모두 정화된다.
# 방의 정보가 주어졌을 때 T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자

#################pypy3##############로 
r, c, t= map(int, input().split())
# 공기 청정기는 -1(두행을 차지)-> 가장 윗행, 아랠행과 두칸이상떨어져있다., 나머지는 미세먼지의 양
board = [list(map(int,input().split())) for _ in range(r)]
front=0 # 공기청정기 윗부분 위치
back=0 # 공기청정기 아래부분 위치

#공기청정기 위치 확인
for i in range(r):
    if board[i][0]==-1:
        front=i
        back=i+1
        break #함수종료조건 잘 잡기


def diffusion():
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    cnt=0
    temp=[[0]*c for _ in range(r)] # 분산된 미세먼지를 기록
    for i in range(r):
        for j in range(c):
            if board[i][j]!=0 and board[i][j]!=-1:
                cnt=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1 :
                        temp[nx][ny]+=board[i][j]//5
                        cnt+=1
                board[i][j]=board[i][j]-board[i][j]//5*cnt #분산되고 남은 미세먼지는 원래 board에 저장

    for i in range(r):
        for j in range(c):
            board[i][j]+=temp[i][j] # 분산된 미세먼지 + 분산되고 남은 미세먼지

# 위쪽 공기청정기 동작
def air_up():
    # 반시계 방향
    dx=[0, -1, 0, 1]
    dy=[1, 0, -1, 0]
    x, y=front, 1
    direction=0
    before=0
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x==front and y==0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            direction = (direction + 1) % 4
            continue
        board[x][y], before = before, board[x][y]
        x, y = nx, ny
def air_down():
    # 반시계 방향
    dx=[0, 1, 0, -1]
    dy=[1, 0, -1, 0]
    x, y=back, 1
    direction=0
    before=0
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x==back and y==0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            direction = (direction + 1) % 4
            continue
        board[x][y], before = before, board[x][y]
        x, y = nx, ny

for _ in range(t):
    diffusion()
    air_up()
    air_down()

result=0
for i in range(r):
    for j in range(c):
        if board[i][j]>0:
            result+=board[i][j]
print(result)
