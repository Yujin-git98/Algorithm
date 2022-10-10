# 19236번 청소년 상어
# 문제 조건에 따라 상어와 물고기의 움직임을 코드로 구현합니다.
# 1. 상어를 0,0에 위치시키고 그 위치의 물고기를 잡어먹습니다.
# 2. 물고기를 순차적으로 조건에 맞게 이동합니다.
# 3. 최근에 잡어먹은 물고기의 방향으로 상어를 이동시킵니다.
# 4. 종료 조건이 될 때까지 2번과 3번을 반복합니다.

#물고기의 이동조건
# 물고기는 작은 번호부터 이동을 시작
# 물고기는 1칸을 이동할 수 있다.
# 이동하려는 칸에 다른 쿨고기가 있으면 서로 위치를 교체한다.
# 이동하려는 칸이 벽이거나 상어가 있다면, 이동가능할 때까지 반시계방향으로 45도 전환을 하고 다시 이동한다.

# 상어의 이동조건
# 상어는 최근에 잡아먹은 물고기의 이동방향을 유지한다.(한번에 1~3칸까지 이동 가능)
# 상어는 물고기가 없는 칸으로 이동할 수 없다.
# 상어가 이동하여 잡아먹을 수 있는 물고기가 없거나 벽을 넘어 이동하면 게임은 종료된다.

# 풀이
# 상어가 먹을 수 있는 물고기 번호의 합이 최댓값을 구해야 한다.
# 상어가 먹을 수 있는 물고기가 여러 개일때 번호가 가장 높은 것을 먹는다고 최종적으로 최댓값이 된다는 보장이 없다
# 따라서 모든 경우에 대해 끝까지 진행하고 최종적으로 판단해야 한다.
import copy
from copy import deepcopy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] ==index: #[0]이 의미하는 것은 번호
                return (i, j)
    return None  # 다 돌았는데 특정한 번호가 없는 경우 none를 return
def move_fish(array, now_x, now_y):
    flag=False
    position=[]
    for i in range(1, 17):
        position=find_fish(array, i)
        if position is None:
            continue # 찾으려고 하는 위치에 물고기가 없으면 잡아먹혔으므로 다음 i로 간다.
        x, y=position[0], position[1]
        dir = array[x][y][1] # [1]이 의미하는 것은 방향 -> 3차원 배열 위치 암기

        # 해당하는 물고기의 방향(dir)에 따라 이동
        for j in range(8):
            nx= x+dx[dir]
            ny= y+dy[dir]
            # 공간 안에서 이동 -> 공간 밖이면 dir를 바꿈
            if 0 <= nx < 4 and 0 <= ny < 4:
                # 이동하려는 곳이 상어가 위치한 곳이 아닐때 아래의 코드를 수행. 상어가 위치한 곳이면 dir를 바꿈
                if not (nx==now_x and ny==now_y): # 공간의 경계, 상어 있는 칸 확인
                    # 물고기가 있으므로 (아까 위에서 없는 경우 제거함) 값을 서로 바꿔줌
                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0] # 번호 교체
                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], dir #방향 교체 # dir은 array[x][y][1]를 의미
                    break # 두번째 for문을 벗어남
            dir=(dir+1)%8
    # 상어가 먹을 수 있는 후보 위치 반환
def food(array, x, y):
    positions=[]
    direction=array[x][y][1]
    for i in range(1, 4):
        nx = x+dx[direction]
        ny = y+dy[direction]
        if 0<=nx<4 and 0<=ny<4 and 1<=array[nx][ny][0]<=16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions


def dfs(array, x, y, total):
    global answer
    array=copy.deepcopy(array)

    # 해당 위치 물고기 먹기
    number=array[x][y][0]
    array[x][y][0]=-1

    # 물고기 이동
    move_fish(array, x, y)

    # 상어가 이동할 수 있는 후보 확인
    result=food(array, x, y)

    # 해당 먹이 먹는 모든 과정 탐색

    for next_x, next_y in result:
        dfs(array, next_x, next_y, total+number)
    answer = max(answer, total + number)

temp = [list(map(int, input().split())) for _ in range(4)]
array = [[None] * 4 for _ in range(4)]
# 배열을 다루기 쉽게 [값, 방향] 형태로 바꾼다.
for i in range(4):
    for j in range(4):
        array[i][j] = [temp[i][j * 2], temp[i][j * 2 + 1] - 1] # -1을 해주는 이유는 방향 배열이 0부터 시작하기 때문
# dfs 탐색
answer=0
dfs(array, 0, 0, 0)
print(answer)
