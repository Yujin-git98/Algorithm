# 19237번 어른 상어
# 상어는 1이상 M이하의 자연수 번호가 붙어있고 모든 번호는 서로 다르다.
# 1의 번호를 가진 어른 상어는 가장 강력, 나머지 모두를 쫓아낸다
# NxN 격자에서 M개의 칸에 상어가 한마리씩 들어있다.
# 맨 처음에는 모든 상어가 자신의 위치에 냄새를 뿌린다.
# 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동. 자신의 냄새를 그 칸에 뿌린다.
# 냄새는 상어가 k번 이동하고 나면 사라진다.

# 상어가 이동 방향을 결정할 때는 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
# 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 이때 가능한 칸이 여러개이면 주어진 우선순위를 따른다.
# 상어의 맨처음 방향은 입력으로 주어지고 그 후에는 방금 이동한 방향이 보고 있는 방향이다.
# 모든 상어가 이동한 후 한 칸에 여러마리의 상어가 남아 있으면 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨남
# 이 과정을 반복할때 1번 상어만 격자에 남게되기까지 몇 초가 걸리는지 구해라
n, m, k = map(int, input().split()) #nxn 격자판, m개 상어 번호, k번 이동하면 냄새사라짐

# 모든 상어의 위치와 방향 정보를 포함하는 2차원 리스트
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보 ***주의 -1을 해서 0부터 시작하거나 1부터 시작하거나
directions = list(map(int, input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 방향 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향 (위, 아래, 왼쪽, 오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 모든 냄새 정보를 업데이트 : 모든 상어가 자신의 위치에 냄새를 뿌린다. 
def update_smell():
    # 각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k] # i, j의 위치에 smell=[상어번호, 냄새 개수]을 넣음

# 1초마다 모든 상어가 이동하고 자신의 냄새를 그 칸에 뿌린다. 
# 모든 상어를 이동시키는 함수
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_array = [[0] * n for _ in range(n)]
    # 각 위치를 하나씩 확인하며
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if array[x][y] != 0:
                # 현재 상어의 방향 #현재 위치의 상어번호(array[x][y])에 대한 우선 순위, 인덱스 맞추기 위해 -1
                direction = directions[array[x][y] - 1]
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4): # 우선순위에서 상어번호(array[x][y]-1),현재 상어방향 , 방향 번호(0~3)
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0:  # 냄새가 존재하지 않는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            # (만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록)
                            # 상어 이동시키기
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True # 냄새가 존재하는 곳으로 이동했는지 여부
                            break
                # 위에서 칸을 찾았는지 안찾았는지 체크하는 단계
                if found: # 냄새가 존재하는곳으로 이동했으면 해당 for문을 넘어간다.
                    continue
                # 모든 칸에 냄새가 차있어서 위에서 움직이지 못했을 경우, 이제 자신의 냄새가 남아있는 칸으로 간다.
                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == array[x][y]:  # 자신의 냄새가 있는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            # 상어 이동 시키기
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array


time = 0
while True:
    update_smell()  # 모든 위치의 냄새를 업데이트
    new_array = move()  # 모든 상어를 이동시키기
    # 상어가 1마리씩 따로 따로 움직이는 것이 아니라 동시에 상어를 다 움직여줘야 한다.
    array = new_array
    time += 1

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False

    # 1번상어만 남았다면 
    if check:
        print(time)
        break

    # 1,000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break
