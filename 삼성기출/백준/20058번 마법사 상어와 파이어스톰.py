# 20058번 마법사 상어와 파이어스톰
# 크기가 2^N × 2^N인 격자
# r, c는 각각 행,열. A[r][c]는 (r, c)에 있는 얼음의 양을 의마한다.
# 파이어스톰을 시전하려면 시전할 때마다 단계 L을 결정해야 한다.
# 격자를 2^Lx2^L 크기의 부분 격자로 나눈다. 그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
# 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. (인접: 상하좌우)
# 마법사 상어는 파이어스톰을 총 Q번 시전하려고 한다. 이후 다음 2가지를 구해보자
# 1. 남아있는 얼음A[r][c]의 합
# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 얼음이 있는칸이 얼음이 있는 칸과 인접해 있으면 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.

# 20058번 마법사 상어와 파이어스톰
#
from copy import deepcopy
from collections import deque
n,q=map(int,input().split()) #2^n x 2^n 격자판, q번 파이어스톰 시전
N=2**n
board=[list(map(int,input().split())) for _ in range(N)]
level=map(int, input().split()) #마법사가 시전한 단계 : 총 q번 있음

for l in level:
    L=2**l # 마법사가 시전한 단계 l를 가져와서 얼마큼의 간격으로 이동해야할지 L을 구해줌.
    # L은 2, 4, 8, 16, 32, 64 등이 가능하며 이는 각각 부분 격자의 모서리(가로길이, 세로길이)라고 보면 된다.
    new_board=deepcopy(board)

    for x in range(0, N, L):
        for y in range(0, N, L): #여기까지가 각 격자를 접근하는 방법
            for i in range(L): #부분 격자 내의 행
                for j in range(L): #부분 격자 내의 열
                    board[x+j][y+L-i-1]=new_board[x+i][y+j]
    new_board=deepcopy(board)

    # 인접한 칸에 얼음이 3개 이상 접해있는지 확인. 그렇지 않으면 얼음의 양이 1만큼 줄어듬
    visited=[[0]*N for _ in range(N)]
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    for x in range(N):
        for y in range(N):
            if board[x][y]>0: #현 위치에 얼음이 0개이면 ***********
                cnt=0
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        if board[nx][ny]>0:
                            cnt+=1 # 인접한 얼음이 있음을 체크. 개수를 저장
                if cnt<3:
                    new_board[x][y]-=1
    board=deepcopy(new_board)


#여기까지 파이어스톰을 q번 실행했다.

# 남아있는 얼음의 합을 구한다.
result1=0
for i in range(N):
    for j in range(N):
        result1+=board[i][j]
print(result1)

# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수

total=0
max_ice=0
for i in range(N):
    for j in range(N):
        if board[i][j]>0: #************중요****************
            q=deque()
            q.append((i, j))
            cnt=0 #덩어리가 차지하는 칸의 개수
            while q:
                x, y=q.popleft()
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        if board[nx][ny]>0:
                            q.append((nx, ny))
                            board[nx][ny]=0 #이미 방문했기 때문에
                            cnt+=1
            max_ice=max(cnt, max_ice)
print(max_ice)






