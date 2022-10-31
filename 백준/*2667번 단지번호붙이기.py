# 백준 2667번 : 단지번호붙이기 == 소프티어 : 장애물 인식 프로그램
# 정사각형 모양의 지도
# 1은 집이 있는 곳, 0은 집이 없는 곳
# 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력해라
from collections import deque
n= int(input()) # 지도의 크기
map=[list(map(int, input())) for _ in range(n)]
num= [] # 각 단지에 속하는 집의 수를 저장

dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]


def bfs(i, j):
    dq=deque()
    dq.append([i, j])
    cnt=1
    visited[i][j]=1
    while dq:
        x, y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==0 and map[nx][ny]==1:
                    cnt+=1
                    visited[nx][ny]=1
                    dq.append([nx, ny])
    return cnt

visited = [[0] * n for _ in range(n)]  # 방문 여부
for i in range(n):
    for j in range(n):
        if map[i][j]==1 and visited[i][j]==0:
            _num=bfs(i, j)
            num.append(_num)

num.sort()
print(len(num))
for i in num:
    print(i)



