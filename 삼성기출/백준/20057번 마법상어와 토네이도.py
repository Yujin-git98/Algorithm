# 20057번 마법사 상어와 토네이도
# NxN 격자인 모래밭에서 위치(r, c)는 격자의 r행 c열을 의미. A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.
# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다.
# 토네이도는 한번에 한칸 이동한다. 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.
# 토네이도가 x에서 y로 이동하면 y의 모든 모래가 비율과 알파가 적혀있는 칸으로 이동한다.
# 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고 계산에서 소수점아래는 버린다.
# 알파는 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다.
# 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다.
# 토네이도는 (1, 1)까지 이동한 뒤 소멸한다.
# 모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때 격자의 밖으로 나간 모래의 양을 구해보자

n=int(input())
data=[list(map(int, input().split())) for _ in range(n)]
x, y=n//2, n//2
dx=[0, 1, 0, -1] # row
dy=[-1, 0, 1, 0] # column

windx = [ #row
    # left
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # down
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # right
    [1, -1, 2, -2, 0, 1, -1, 1, -1],
    # up
    [1, 1, 0, 0, -2, 0, 0, -1, -1]
]
windy = [ #column
    # left
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    # down
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # right
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # up
    [1, -1, 2, -2, 0, 1, -1, 1, -1]
]

rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]

def wind(x, y, dir):
    value=0
    sand=data[x][y] # 현재 모래의 양을 초기화
    sum_value=0
    for i in range(9):
        nx=x+windx[dir][i]
        ny=y+windy[dir][i]
        wind_sand = (sand*rate[i]) //100 # 현재 모래의양에 비율을 곱해서 wind_sand에 저장
        sum_value+=wind_sand # 9개바향의 모래의 양을 sum_value에 저장

        #if nx<0 or ny<0 or nx>=n or ny>=n: 아래와 같은 의미
        if not(0<=nx<n and 0<=ny<n): #격자판 밖으로 나가는 것은 value에 따로 저장
            value+=wind_sand
            continue
        data[nx][ny]+=wind_sand # 격자판의 모래를 업데이트 해줌

    # 9번의 작업을 다수행했으면 알파(a)에 위치 (nx, ny)하는 모래의 양을 구하기 위해
    # (x, y)의 좌표의 모래의 양에서 옮긴 모래의 총합(sum_value)를 빼준다.

    nx=x+dx[dir]
    ny=y+dy[dir]
    a = sand-sum_value
    # 알파의 위치가 범위를 벗어난다면 value값에 알파값을 더해주고
    # 범위 내에 있다면 이동가능하므로 data[nx][ny]에 알파를 더해준다.
    if not(0<=nx<n and 0<=ny<n):
        value+=a
    else:
        data[nx][ny]+=a
    data[x][y]=0
    return value
    # 이후 현재좌표(x, y)값을 0으로 갱신한 후 value값을 방환한다


def snail(x, y):
    direction=-1
    value=0
    visited=[[0]*n for _ in range(n)]
    while True:
        if x== 0 and y==0:
            break
        else:
            visited[x][y]=1 #현재 위치 방문 체크
            nd=(direction+1)%4 # 방향을 바꿈
            nx=x+dx[nd]     # 바꾼 방향으로 좌표 생성
            ny=y+dy[nd]

        if visited[nx][ny]: # 생성한 좌표가 이전에 방문한 곳이면
            nd=direction    # 이전 방향을 가져옴
            nx = x + dx[nd] # 이전 방향으로 좌표 생성
            ny = y + dy[nd]
        value += wind(nx, ny, nd) # 생성한 바꾼 방향을 알려줌
        x, y, direction = nx, ny, nd # 현재 좌표 및 방향 업로드
    return value
result=snail(x, y)
print(result)


