# 4963번 섬의 개수
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어지고 섬의 개수를 세는 프로그램을 작성하시오
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
# 지도 밖으로 나갈 수 없다.
# 입력은 여러 개의 테스트 케이스로 이루어져 있음
# 각 테스트 케이스의 첫번째 줄은 지도의 너비 w와 높이 h가 주어진다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다
# 입력의 마지막 줄에는 0이 2개 주어진다.
from collections import deque
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(i, j, visited, graph):
    dq=deque()
    dq.append([i,j])
    visited[i][j]=1 # 방문 처리
    while dq:
        x,y = dq.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    dq.append([nx, ny])

    return 1

while True:
    w, h = map(int, input().split()) # 행은 h, 열은 w
    if w==h==0:
        break
    graph=[]
    for _ in range(h):
        graph.append(list(map(int,input().split()))) # graph(지도)의 값을 저장. 1은 땅, 0은 바다
    visited=[[0]*w for _ in range(h)]
    result=0

    for i in range(h): # 행
        for j in range(w): # 열
            if visited[i][j]==0 and graph[i][j]==1: # 방문하지 않은 곳이여야 하고, graph(지도)가 땅이여야 함.
                result+=bfs(i, j, visited, graph)

    print(result)

