# 21610번 마법사 상어와 비바라기
# 격자 nxn, r행 c열,
# A[r][c]는 (r,c)에 있는 바구니에 저장되어 있는 물의양
# 1번 행과 N번 행을 연결, 1번 열과 N번 열도 연결.
# 즉, N번 행의 아래에는 1번 행이 있고, 1번행 위에 N번행이 있다.
# 1번열 왼쪽에는 N번 열이, N번열의 오른쪽에는 1번 열이 있다.
# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
# 구름에 이동을 M번 명령한다. i번쨰 이동 명령은 방향 di와 거리 si로 이루어져 있다.
# 방향은 총 8개 방향이 있으며, 1부터 순서대로 좌, 좌상, 상, 상우, 우, 우하, 하,하좌

# 1. 모든 구름이 di방향으로 si 칸 이동한다
# 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니 물이 1증가한다
# 3. 구름이 모두 사라진다.
# 4. 2에서 물이 증가한 칸(r, c)에 물복사버그 마법을 시전한다.
# 이는 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물의 양이 증가한다.
#   이때 이동과 다르게 경계를 넘어 가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
#   예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
#   -> 여기서 bfs나 dfs 사용해야할 듯
# 5.바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다
# 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
#M번 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자
from collections import deque
dx=[0, -1, 1, -1, 0, 1, 1, 1]
dy=[-1,-1, 0, 1, 1, 1, 0, -1]


n, m = map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)] #n개의 줄에 n개의 정수
d=[] # 방향
s=[] # 거리
for i in range(m):
    a, b = map(int, input().split())
    d.append(a-1)
    s.append(b)
cloud_visited=[[0]*n for _ in range(n)] # 구름은 한번 방문한 칸은 1로 체크하기
cloud_pos=[[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]] # 구름의 위치 [[n, 1], [n, 2], [n-1, 1], [n-1, 2]]에서 각각 1씩 빼준값

# 1. 모든 구름이 방향 d으로 s칸 이동한다.
for i in range(m): #d,s가 0번부터 m번까지 제공
    water_plus = [[0] * n for _ in range(n)]  # 물이 증가한 곳을 체크 / 구름이 이동 때마다 초기화
    for j in range(len(cloud_pos)): #구름위치가 0~3번째일 때 어떻게 이동하는지
        cloud_pos[j][0]=(cloud_pos[j][0]+dx[d[i]]*s[i])%n #방향은 d[i]이고 거리는 s[i]만큼 이동한다.
        cloud_pos[j][1]=(cloud_pos[j][1]+dy[d[i]]*s[i])%n #n으로 나누는 이유는 서로 연결되어 있기 때문
        cloud_x=cloud_pos[j][0]
        cloud_y=cloud_pos[j][1]
        # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        board[cloud_x][cloud_y]+=1
        # 구름이 사라진다.
        #cloud_pos=[[0]*2 for _ in range(4)]
        # 구름이 생겼다가 사라지는 경우를 저장한다
        cloud_visited[cloud_x][cloud_y]=1 # 구름이 생겼다 사라진 곳을 체크
        water_plus[cloud_x][cloud_y] = 1  # 물의 양이 1 증가한 곳


    # 2.에서 물이 증가한 칸(r,c)에 물복사 마법 시작 ->  갈 수 있는 대각선 방향을 모두 구하기
    cnt=0 # 대각선 방향에 물이 있는 경우
    ddx=[-1, -1, 1, 1]
    ddy=[-1, 1, 1, -1]
    for i in range(n):
        for j in range(n): #(i, j) 좌표
            cnt = 0
            if water_plus[i][j]==1: #물이 증가한 칸에 대해서만 대각선 반향 조사
            #if cloud_visited[i][j] == 1:  # 물이 증가한 칸에 대해서만 대각선 반향 조사
                for k in range(4):
                    nx=i+ddx[k]
                    ny=j+ddy[k]
                    if 0<=nx<n and 0<=ny<n: #격자 안에 있는 경우만 추가
                        if board[nx][ny]>0: #대각선 방향에 물이 있는 경우
                            cnt+=1

                board[i][j]+=cnt # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수만큼 물의 양이 증가한다.


    for _ in range(len(cloud_pos)):
        cloud_pos.pop()
    for i in range(n):
        for j in range(n):
            if board[i][j]>=2:
                #if cloud_visited[i][j]!=1:
                if water_plus[i][j] != 1:
                    board[i][j]-=2
                    cloud_pos.append([i,j])
result=0
for i in range(n):
    for j in range(n):
        if board[i][j]>0:
            result+=board[i][j]


print(result)
