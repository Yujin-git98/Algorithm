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
from collections import deque
from copy import deepcopy
n, q=map(int, input().split()) # nxn격자, q번 파이어스톰 시전
board=[list(map(int, input().split())) for i in range(2**n)]
level=list(map(int, input().split()))

for lev in level:
    L=2**lev
    new_board = deepcopy(board)
    for x in range(0, 2**n, L):
        for y in range(0, 2**n, L):
            for i in range(L):
                for j in range(L):
                    new_board[x+j][y+L-i-1]=board[x+i][y+j]
    board=deepcopy(new_board)

    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]

    # 인접한 얼음 카운팅
    check = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
    for x in range(2**n):
        for y in range(2**n):
            cnt=0
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if (0<=nx<2**n and 0<=ny<2**n):
                    if board[nx][ny]>0:
                        cnt+=1
            # 얼음 제거
            if cnt<3:
                if board[nx][ny]>0: # 얼음의 개수가 -가 되면 안되니까
                    #board[nx][ny]-=1
                    check[nx][ny] = 1

    for r in range(2 ** n) :
        for c in range(2 ** n) :
            if check[r][c] :
                board[r][c] -= 1

# 남아있는 얼음의 합 출력
result1=0
for i in range(2**n):
    for j in range(2**n):
        result1+=board[i][j]
print(result1)

# (x, y)가 속한 덩어리의 크기:bfs사용
def bfs(cx, cy):
    q=deque()
    q.append((cx, cy))
    size=1

    visited[cx][cy]=1
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<2**n and 0<=ny<2**n:
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx, ny))
                    size+=1
    return size

# 제일 큰 덩어리를 구해라
result2=0
for x in range(2**n):
    for y in range(2**n):
        if board[x][y]>0:
            visited = [[0] * (2 ** n) for _ in range(2 ** n)]
            result2=max(result2, bfs(x, y))
print(result2)



"""def rotate(cx, cy, len, unit):
    if len==unit: # len이 unit과 같아지면 90도 회전시킨다.
        new_board=[[0]*len for _ in range(len)]
        for x in range(len):
            for y in range(len):
                new_board[cx+y][cy+len-x-1]=board[cx+x][cy+y]
        for x in range(len):
            for y in range(len):
                board[cx + x][cy + y]=board[cx+x][cy+y]
        return
    else:
        len=len//2
        rotate(cx, cy, len, unit)
        rotate(cx+len, cy, len, unit)
        rotate(cx, cy+len, len, unit)
        rotate(cx+len, cy+len, len, unit)

for i in range(q):
    if level[i]>0:
        rotate(0, 0, int(2**n), int(2**level[i]))"""










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
from collections import deque
from copy import deepcopy
n, q=map(int, input().split()) # nxn격자, q번 파이어스톰 시전
board=[list(map(int, input().split())) for i in range(2**n)]
level=list(map(int, input().split()))

for lev in level:
    L=2**lev
    new_board = deepcopy(board)
    for x in range(0, 2**n, L):
        for y in range(0, 2**n, L):
            for i in range(L):
                for j in range(L):
                    new_board[x+j][y+L-i-1]=board[x+i][y+j]
    board=deepcopy(new_board)

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

# 인접한 얼음 카운팅
for x in range(2**n):
    for y in range(2**n):
        cnt=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<2**n and 0<=ny<2**n):
                if board[nx][ny]>0:
                    cnt+=1
        # 얼음 제거
        if cnt<3:
            if board[nx][ny]>0: # 얼음의 개수가 -가 되면 안되니까
                board[nx][ny]-=1
# 남아있는 얼음의 합 출력
result1=0
for i in range(2**n):
    for j in range(2*n):
        result1+=board[i][j]
print(result1)

# (x, y)가 속한 덩어리의 크기:dfs 사용
def dfs(x, y):
    size=1
    board[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<2**n and 0<=ny<2**n:
            size+=dfs(nx, ny)
    return size

# (x, y)가 속한 덩어리의 크기:bfs사용
def bfs(cx, cy):
    q=deque()
    q.append((cx, cy))
    size=1
    visited =[[0]*(2 ** n) for _ in range(2 ** n)]
    visited[cx][cy]=1
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<2**n and 0<=ny<2**n:
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx, ny))
                    size+=1
    return size

# 제일 큰 덩어리를 구해라
result2=0
for x in range(2**n):
    for y in range(2**n):
        if board[x][y]>0:
            result2=max(result2, dfs(x, y))
print(result2)



"""def rotate(cx, cy, len, unit):
    if len==unit: # len이 unit과 같아지면 90도 회전시킨다.
        new_board=[[0]*len for _ in range(len)]
        for x in range(len):
            for y in range(len):
                new_board[cx+y][cy+len-x-1]=board[cx+x][cy+y]
        for x in range(len):
            for y in range(len):
                board[cx + x][cy + y]=board[cx+x][cy+y]
        return
    else:
        len=len//2
        rotate(cx, cy, len, unit)
        rotate(cx+len, cy, len, unit)
        rotate(cx, cy+len, len, unit)
        rotate(cx+len, cy+len, len, unit)

for i in range(q):
    if level[i]>0:
        rotate(0, 0, int(2**n), int(2**level[i]))"""


